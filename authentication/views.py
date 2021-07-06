from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
#from .models import UserContacts
#user_contacts = UserContacts.objects.all

def login_user(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['password']
		email_address = str(username)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('catalogue')
		else:
			messages.success(request, ('Error logging in. Please try again and check to ensure you have entered the right credentials'))
			return redirect('login')
	else:
	    return render(request, 'authentication/login.html', {})
    
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			phone_number = form.cleaned_data['phone_number']
			user = form.save()

			#user = authenticate(username=user_name, password=password)
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('catalogue')
		if form.errors == "My customers with this email address already exists":
			form.errors == "User with that email address exists"
	else:
		form = SignUpForm()
	context = {'form':form}
	return render(request, 'authentication/register.html', context)

def logout_user(request):
	logout(request)
	return redirect('catalogue')
# Create your views here.
