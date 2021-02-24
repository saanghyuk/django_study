from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
  username = forms.CharField(max_length=32, label="사용자 이름", error_messages={'required': '아이디를 입력해 주세요'}, help_text="32자 이내로 입력해주세요.")
  useremail=forms.CharField(widget=forms.EmailInput, max_length=32, label="사용자 이메일", error_messages={'required': '이메일을 입력해 주세요'}, help_text="32자 이내로 입력해주세요.")
  password = forms.CharField(widget=forms.PasswordInput, label = "비밀번호", error_messages={'required': '비밀번호를 입력해 주세요'}, help_text="길이 무제한")
  re_password = forms.CharField(widget=forms.PasswordInput, label = "비밀번호 확인", error_messages={'required': '비밀번호를 한번 더 입력해 주세요'}, help_text="길이 무제한")

  def clean(self):
    cleaned_data = super().clean()
    username = cleaned_data.get('username')
    useremail = cleaned_data.get('useremail')
    # password = cleaned_data.get('password')
    # re_password = cleaned_data.get('re_password')

    if Fcuser.objects.filter(username = username).count():
      self.add_error('username', '사용자명이 존재합니다.')
    elif Fcuser.objects.filter(useremail = useremail).count():
      self.add_error('useremail', '이메일이 존재합니다.')
    else:
      pass

class LoginForm(forms.Form):
  username = forms.CharField(max_length=32, label="사용자 이름", error_messages={'required': '아이디를 입력해 주세요'}, help_text="32자 이내로 입력해주세요.")
  password = forms.CharField(widget=forms.PasswordInput, label = "비밀번호", error_messages={'required': '비밀번호를 입력해 주세요'}, help_text="길이 무제한")

  def clean(self): #is_valid를 호출하면 자동으로 호출됨.
    cleaned_data = super().clean()
    username = cleaned_data.get('username')
    password = cleaned_data.get('password')


    if username and password:
      try:
        fcuser = Fcuser.objects.get(username = username)
      except Fcuser.DoesNotExist:
        self.add_error('username', '아이디가 없습니다.')
        return

      if not check_password(password, fcuser.password):
        self.add_error('password', '비밀번호가 틀렸습니다.') #password.errors에 자동으로 들어감.

      else:
        self.user_id = fcuser.id


