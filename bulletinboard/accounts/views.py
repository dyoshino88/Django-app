from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from .models import UserActiveTokens
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def home(request):
  return render(
    request, 'accounts/home.html'
  )
  
def registration(request):
  registration_form = forms.RegistrationForm(request.POST or None)
  if registration_form.is_valid():
    try:
      registration_form.save()
      messages.success(request, 'ご入力いただいたメールアドレスに本会員登録用のメールを送信しました。')
      return redirect('accounts:home')
    except ValidationError as e:
      registration_form.add_error('password', e) 
  return render(
    request, 'accounts/registration.html', context={
      'registration_form':registration_form,
    }
  )

def active_user(request, token):
  user_active_token = UserActiveTokens.objects.active_user_using_token(token) 
  return render(
    request, 'accounts/active_user.html'
  )

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

# メール設定
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.timezone import datetime, timedelta
from uuid import uuid4
from django.contrib.auth.models import User 
from .models import UserActiveTokens

def send_email_view(request):
    if request.method == 'POST':
        # フォームから入力されたメールアドレスとユーザ名を取得
        recipient_email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        
        # ユーザを作成（ユーザが存在しない場合のみ）
        user, created = User.objects.get_or_create(username=username)

        # メールを送信する
        subject = '本会員登録のご案内'
        user_active_token = UserActiveTokens.objects.create(
        r_user=user, 
        token=str(uuid4()),
        expired_time=datetime.now() + timedelta(hours=5)
        )
        message = f'会員登録ありがとうございます。以下のURLをクリックされますとユーザー認証が完了しますので、完了後、ログインをお願い致します。https://dkoukan.com/accounts/active_user/{user_active_token.token}'
        from_email = 'yoshino0707dh@gmail.com'
        recipient_list = [recipient_email]

        send_mail(subject, message, from_email, recipient_list)

        # メール送信後に何らかの処理を行う場合はここに追加

        return HttpResponse('メールを送信しました。')
    
    # GETリクエストの場合は単にテンプレートを表示
    return render(request, 'send_email_form.html')
  
  
# views.py

from django.shortcuts import render
from ..utils import send_email

def send_email_view(request):
    # 送信処理のコード
    # ...

    # メールを送信する
    subject = '本会員登録のご案内'
    message = '会員登録ありがとうございます。以下のURLをクリックされますとユーザー認証が完了します。'
    recipient_list = ['recipient@example.com']

    status_code = send_email(subject, message, recipient_list)

    if status_code == 202:
        return HttpResponse('メールを送信しました。')
    else:
        return HttpResponse('メールの送信に失敗しました。')
