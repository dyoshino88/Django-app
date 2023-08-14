from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password
# 以下追加
from django.forms.widgets import SelectDateWidget

class RegistrationForm(forms.ModelForm):
  username = forms.CharField(label='ユーザーネーム')
  date_of_birth = forms.DateField(
    label='誕生日',
    widget=SelectDateWidget(years=range(1900, 2023)),
    )
  email = forms.EmailField(label='メールアドレス')
  password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
  reenter_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

  class Meta():
    model = User
    fields = ('username', 'date_of_birth', 'email', 'password')

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data['password']
    reenter_password = cleaned_data['reenter_password']
    if password != reenter_password:
      raise forms.ValidationError('パスワードが違います。再度入力してください。')

  def save(self, commit=False):
    r_user = super().save(commit=False)
    validate_password(self.cleaned_data['password'], r_user)
    r_user.set_password(self.cleaned_data['password'])
    r_user.save()
    return r_user

class LoginForm(forms.Form): 
  email = forms.CharField(label="メールアドレス")
  password = forms.CharField(label="パスワード", widget=forms.PasswordInput())

class UserEditForm(forms.ModelForm): 
  username = forms.CharField(label='ユーザーネーム')
  date_of_birth = forms.DateField(label='誕生日')
  email = forms.EmailField(label='メールアドレス')
  picture = forms.FileField(label='写真', required=False)

  class Meta:
    model = User
    fields = ('username', 'date_of_birth', 'email', 'picture')

class ChangePasswordForm(forms.ModelForm):
    
  password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
  reenter_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

  class Meta():
    model = User
    fields = ('password',)

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data['password']
    reenter_password = cleaned_data['reenter_password']
    if password != reenter_password:
      raise forms.ValidationError('パスワードが違います。再度入力してください。')

  def save(self, commit=False):
    r_user = super().save(commit=False)
    validate_password(self.cleaned_data['password'], r_user)
    r_user.set_password(self.cleaned_data['password'])
    r_user.save()
    return r_user