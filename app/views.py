from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth import login, authenticate  , logout 
from django.contrib.auth.forms import AuthenticationForm

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
        	username = form.cleaned_data.get('username')
        	password = form.cleaned_data.get('password')
        	user = authenticate(username=username, password=password)
        	if user is not None:
        		login(request, user)
        		messages.info(request, f"You are now logged in as {username}.")
        		return redirect('pro')
        	else:
        		messages.error(request,"Invalid username or password.")
    else:
    	form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
    
    
#@login_required(redirect_field_name = 'register', login_url = 'login')   
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
		#print(form)
	return render(request,'user/register.html', {'form': form})


@login_required(redirect_field_name = 'pro', login_url = 'login')
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST or None, instance=request.user)
		p_form = ProfileUpdateForm(request.POST ,request.FILES ,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('pro')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		'u_form': u_form,
		'p_form': p_form,
	}

	return render(request, 'profile.html', context)
def logout_user(request):
    logout(request)
    return redirect('login')
    
# Create your views here.
