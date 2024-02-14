from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout, authenticate
from .forms import *
#prevents certain pages from being seen without proper login
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

#_______________________________________________________________________
@login_required
def home(request):
    return render(request, 'home.html')

#______________________________________________________________________
def register(request):
    if request.method =='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

#_______________________________________________________________________
def Custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home
                return redirect('home')
            else:
                # Handle authentication error, e.g., display an error message
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

#_______________________________________________________________________
def account_view(request):
    # Add any necessary logic here
    return render(request, 'webs/account.html')

#_______________________________________________________________________
def activity_view(request):
    # Add any necessary logic here
    return render(request, 'webs/activity.html')

#_______________________________________________________________________
def diet_view(request):
    # Add any necessary logic here
    return render(request, 'webs/diet.html')

#_______________________________________________________________________
def composition_view(request):
    # Add any necessary logic here
    return render(request, 'webs/composition.html')

#_______________________________________________________________________
def routine_view(request):
    # Add any necessary logic here
    return render(request, 'webs/routine.html')