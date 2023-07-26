from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from .models import UserActiveTokens
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.utils.timezone import datetime, timedelta
from uuid import uuid4
from django.conf import settings
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/home.html')

def registration(request):
  registration_form = forms.RegistrationForm(request.POST or None)
  if registration_form.is_valid():
    try:
      user = registration_form.save()
      
      # ユーザの認証トークン作成
      user_active_token = UserActiveTokens.objects.create(
        r_user = user,
        token = str(uuid4()),
        expired_time = datetime.now() + timedelta(hours=5)
      )
      
      # 認証メール送信
      subject = '本会員登録のご案内'
      message = f'会員登録ありがとうございます。以下のURLをクリックされますとユーザー認証が完了しますので、完了後、ログインをお願い致します。https://dkoukan.com/accounts/active_user/{user_active_token.token}'
      from_email = settings.DEFAULT_FROM_EMAIL
      recipient_list = [user.email]
      
      send_mail(subject, message, from_email, recipient_list)
      
      message.success(request, 'ご入力いただいたメールアドレスに本会員登録用のメールを送信しました。')
      return redirect('accounts:home')
    except ValidationError as e:
      registration_form.add_error('password', e)

  return render(
    request, 'accounts/registration.html',context={
      'registration_form': registration_form,
    }
  )    
      
def active_user(request, token):
  try:
    user_active_token = UserActiveTokens.objects.get(token=token, expired_time__gt=datetime.now())
    user = user_active_token.r_user
    user.is_active = True
    user.save()
    messages.success(request, 'ユーザ認証が完了しました。ログインしてください。')
    return redirect('accounts:login_page')
  except UserActiveTokens.DoesNotExist:
    messages.error(request, '無効な認証です。')
    return redirect('accounts:home')

def login_page(request): 
  login_form = forms.LoginForm(request.POST or None)
  if login_form.is_valid():
    email = login_form.cleaned_data.get('email')
    password = login_form.cleaned_data.get('password')
    r_user = authenticate(email=email, password=password)
    if r_user:
      if r_user.is_active:
        login(request,r_user)
        messages.success(request, 'ログインに成功しました')
        if 's1' in request.session:
          s1 = request.session['s1']
        else:
          s1 = 'hello'
          request.session['s1'] = s1
        params = {'s1': s1}
        return render(request,'accounts/home.html', params)
      else:
        messages.warning(request, 'ユーザが無効です。')
    else:
      messages.warning(request, 'メールアドレスまたはパスワードが違います')
  return render(
    request, 'accounts/login_page.html', context={
      'login_form':login_form,
    }
  )

@login_required
def logout_page(request):
  logout(request)
  messages.success(request, 'ログアウトしました')
  return redirect('accounts:home')

@login_required 
def edit_page(request):
  edit_form = forms.UserEditForm(
    request.POST or None, 
    request.FILES or None, 
    instance = request.user
    )
  if edit_form.is_valid():
    messages.success(request, '更新されました')
    edit_form.save()
  return render(request, 'accounts/edit_page.html', context={
      'edit_form': edit_form,
  })
  
@login_required
def change_password(request):
  change_password_form = forms.ChangePasswordForm(request.POST or None, instance=request.user) 
  if change_password_form.is_valid():
    try:
      change_password_form.save()
      messages.success(request, 'パスワードが更新されました')
      update_session_auth_hash(request, request.user)
    except ValidationError as e:
      change_password_form.add_error('password', e)
  return render(
    request, 'accounts/change_password.html', context={
      'change_password_form': change_password_form,
    }
  )

def error_page(request, exception):
  return render(
    request, '404.html'
  )
  
def my_error_handler(request, *args, **kw):
  import sys
  from django.views import debug
  from django.http import HttpResponse
  error_html = debug.technical_500_response(request, *sys.exc_info()).content
  return HttpResponse(error_html)

# 認証メール設定

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.timezone import datetime, timedelta
from uuid import uuid4
from .models import UserActiveTokens
from django.conf import settings
from django.http import HttpResponse

def user_registration_view(request):
    if request.method == 'POST':
        # フォームから入力されたデータを取得
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')

        # ユーザを作成 (パスワードの処理を追加することも可能)
        user, created = User.objects.get_or_create(username=username, email=email)

        # ユーザの認証トークンを作成
        user_active_token = UserActiveTokens.objects.create(
            r_user=user,
            token=str(uuid4()),
            expired_time=datetime.now() + timedelta(hours=5)
        )

        # 認証メールを送信
        subject = '本会員登録のご案内'
        message = f'会員登録ありがとうございます。以下のURLをクリックされますとユーザー認証が完了しますので、完了後、ログインをお願い致します。https://dkoukan.com/accounts/active_user/{user_active_token.token}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return HttpResponse('メールを送信しました。')
    
    # GETリクエストまたは不正なフォーム送信の場合
    return render(request, 'accounts/registration.html')

