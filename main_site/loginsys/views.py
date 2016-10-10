from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    params = {}
    params.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            params['login_error'] = 'User not found'
            return render_to_response('loginsys/login.html', params)
    else:
        return render_to_response('loginsys/login.html', params)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    params = {}
    params.update(csrf(request))
    params['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            params['form'] = newuser_form
    return render_to_response('loginsys/register.html', params)


def login_required(request):
    return render_to_response('loginsys/login_required.html')
