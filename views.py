from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def home(request):
	return render(request,'home.html')
def login(request):
	if request.method == 'POST':
		user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'login.html',{'error':'username or password is invalid'})

	else:
		return render(request,'login.html')

def register(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user=User.objects.get(username=request.POST['username'])
				return render(request,'register.html',{'error':'Username has been taken'})

			except User.DoesNotExist:
				user=User.objects.create_user(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],username=request.POST['username'],password=request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request,'register.html',{'error':'password must match'})


	else:
		return render(request,'register.html')

def logout(request):
	return redirect('register')
