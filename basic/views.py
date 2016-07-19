from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm

def log_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    args = {}
    args.update(csrf(request))
    return render(request, 'basic/login.html', args)

def auth_view(request):
    username = request.POST.get('inputUsername', "")
    password = request.POST.get('inputPassword', "")
    user  = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect('/')
    else:
        messages.warning(request, 'Invalid Credentials.')
        return HttpResponseRedirect('/accounts/login')

@login_required(login_url='/accounts/login/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')

def register(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        flag = 0
        if User.objects.filter(username=request.POST.get('username')).exists():
            messages.warning(request, 'Username already exists!')
            flag = 1
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.warning(request, 'Someone is already registered with this email!')
            flag = 2
        if form.is_valid() and flag == 0:
            form.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            
            return HttpResponseRedirect('/accounts/register')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = RegistrationForm()
        return render(request, 'basic/register.html', args)

def landing(request):
    return render(request, 'basic/landing.html')