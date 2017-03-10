from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserProfileForm


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
    # if request.user:
        # print(request.user, request.user.id)
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


def login_need(request):
    return render_to_response('loginsys/login_required.html')


@login_required
def user_page(request):
    params = {}
    current_user = User.objects.get(id=auth.get_user(request).id)
    params['favorite_books'] = current_user.profile.favorites.all()
    return render(request, template_name='loginsys/userpage.html', context=params)


@login_required
def edit_user_profile(request):
    params = {}
    params.update(csrf(request))
    current_user = User.objects.get(id=auth.get_user(request).id)
    params['form'] = UserProfileForm(instance=current_user.profile)

    if request.POST:
        edit_user_profile_form = UserProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if edit_user_profile_form.is_valid():
            edit_user_profile_form.save()
            return redirect("/auth/account/")
        else:
            params['form'] = edit_user_profile_form
    else:
        return render(request,
                      template_name='loginsys/edit_user_profile.html',
                      context=params)
