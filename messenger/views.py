from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from messenger.forms import NewUserForm


def index(request):
    if request.user.is_authenticated:
        return render(request, 'default.html')
    else:
        return HttpResponseRedirect('auth')


def auth(request):
    return render(request, 'auth.html', {'form': NewUserForm()})


def registration(request):
    print("registration")
    print("request.POST", request.POST)

    if request.POST:
        form = NewUserForm(request.POST)

        if form.is_valid():
            print("form is valid")
            user = form.save()
            login(request, user)
        elif form.errors:
            print(form.errors)
            messages.error(request, "Unsuccessful registration. Invalid information.")
        else:
            return HttpResponseRedirect('/')

    return render(request, 'registration.html', {'form': UserCreationForm()})