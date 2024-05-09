from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token 
import io
from .utils import translateGG, speech2text,translate, summarizer,summariseForYoutube
from pydub import AudioSegment
import time
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import datetime as dt
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from .forms import RegisterForm,LoginForm,PasswordChangeForm1
from .models import RecordUser, RecordSpeechText
import tempfile 

def get_home(request):
    context = {}
    context['token'] = request.session.get('token', '')
    return render(request, 'home.html',context)

def get_contact(request):
    return render(request, 'contact.html')

def get_teams(request):
    return render(request, 'teams.html')
    
def login_required_if_authenticated(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return login_required(view_func)(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view


def redirect_authenticated_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view

@method_decorator(redirect_authenticated_user, name='dispatch')
class RegisterView(FormView):
    template_name = 'account/sign_up.html'
    form_class = RegisterForm
    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(form.cleaned_data['password'])
        user.save()
        username = user.username
        messages.success(self.request, f'Account created for {username}')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('login')

class LoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    authentication_form = LoginForm
    # success_url = reverse_lazy('home')
    def form_valid(self, form):
        login(self.request, form.get_user())
        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)  
        token, _ = Token.objects.get_or_create(user=self.request.user)
        self.request.session['token'] = token.key
        return super().form_valid(form)
    
    @method_decorator(login_required_if_authenticated)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('home')
from django.views import View

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if 'token' in self.request.session:
            self.request.session['token'] = 'None'
        logout(request)
        return redirect('home')
    
class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    form_class = PasswordChangeForm1
    # success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('home')