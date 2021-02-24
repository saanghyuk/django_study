from django.shortcuts import render, redirect
from .models import Fcuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm, RegisterForm
# Create your views here.

def home(request):
  user_id = request.session.get('user')
  if user_id :
    fcuser = Fcuser.objects.get(pk=user_id)
    return HttpResponse(fcuser.username+'님 안녕하세요!')
  return HttpResponse('Home님')


def logout(request):
  if request.session.get('user'):
    del(request.session['user'])

  return redirect('/')


def login(request):
    if request.method =='POST':
      form = LoginForm(request.POST)
      if form.is_valid(): #valid(값이 들어있는지 아닌지 판단)하지 않으면, form.error로 error가 들어감
        #session code
        request.session['user']=form.user_id
        return redirect('/')
    else:
      form = LoginForm()

    return render(request, 'login.html', {'form':form})



def register(request):
  if request.method =='POST':
    form = RegisterForm(request.POST)
    error=""
    if form.is_valid():
      username = request.POST.get('username', None)
      useremail = request.POST.get('useremail', None)
      password = request.POST.get('password', None)
      re_password = request.POST.get('re_password', None)

      # if not (username and useremail and password and re_password):
        # error = '모든 항목을 입력해주세요.'
      if password != re_password:
        error = '비밀번호가 서로 다릅니다.'
      else:
        fcuser = Fcuser(
          username = username,
          password = make_password(password),
          useremail = useremail
        )
        fcuser.save()
        request.session['user']=fcuser.id

        return redirect('/')

    return render(request, 'register.html', {'form':form, 'error':error})

  else:
      form = RegisterForm()
      return render(request, 'register.html', {'form':form} )