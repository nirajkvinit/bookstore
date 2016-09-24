from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
# from django.contrib.auth.forms import UserCreationForm


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


# def register(request):
    # params = {}
    # params.update(csrf(request))
    # params['form'] = UserCreationForm()
    # if request.POST:
        # newuser_form = UserCreationForm(request.POST)
        # newuser_form.save()
        # newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password'], email=newuser_form.cleaned_data['email'])
        # auth.login(request, newuser)
        # return redirect('/')
    # return render_to_response('register.html', params)
