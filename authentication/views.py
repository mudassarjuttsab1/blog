from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth import login, authenticate, logout
from django.views import View
from . import forms
from django.conf import settings
from pdb import set_trace
from django.contrib import messages

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class LoginView(View):
    template_name = 'authentication/login.html'
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        set_trace()
        messages = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages = 'Login failed!'
        return render(request, 'authentication/login.html', {'form': form, 'message': message})

class SignUpView(View):
    def get(self,request):
        form = forms.SignupForm()
        return render(request,'authentication/signup.html',{'form': form})
    def post(Self,request):

        form = forms.SignupForm()
        if request.method == 'POST':
            form = forms.SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                # auto-login user
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, 'authentication/signup.html', context={'form': form})
