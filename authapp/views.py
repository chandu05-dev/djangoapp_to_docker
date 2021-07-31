from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/auth/signupsuccess")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	
	return render (request=request, template_name="authapp/register.html", context={"register_form":form})


def signupsuccess(request):
	return render (request=request, template_name="authapp/succes.html")


def mylogin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/polls")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="authapp/login.html", context={"login_form":form})




def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/auth/mylogin")







