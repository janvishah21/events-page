from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
       	    messages.error(request, 'Authentication Failed !', extra_tags='alert alert-warning alert-dismissible fade show')
            form = AuthenticationForm(request.POST)
            return render(request, 'user/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'user/signin.html', {'form': form})


def signout(request):
	logout(request)
	return redirect('/')


def signup(request):
	if request.method == 'POST':
		check1 = False
		check2 = False
		check3 = False
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			username = form.cleaned_data['username']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			email = form.cleaned_data['email']

			if password1 != password2:
				check1 = True
				messages.error(request, 'Password doesn\'t matched', extra_tags='alert alert-warning alert-dismissible fade show')
			if User.objects.filter(username=username).exists():
				check2 = True
				messages.error(request, 'Username already exists', extra_tags='alert alert-warning alert-dismissible fade show')
			if User.objects.filter(email=email).exists():
				check3 = True
				messages.error(request, 'Email already registered', extra_tags='alert alert-warning alert-dismissible fade show')

			if check1 or check2 or check3:
				messages.error(request, "Registration Failed", extra_tags='alert alert-warning alert-dismissible fade show')
				return redirect('user:signup')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=name)
				messages.success(request, f'Thanks for registering {name}!', extra_tags='alert alert-success alert-dismissible fade show')
				return redirect('user:signin')
	else:
		form = AuthenticationForm()
	return render(request, 'user/signup.html', {'form': form})