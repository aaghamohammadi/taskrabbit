from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from user.forms import CustomerRegForm, LoginForm


def index(request):
    return render(request, 'index.html', {})


def registration(request):
    if request.method == "POST":
        if 'member-reg-btn' in request.POST:
            customer_reg_form = CustomerRegForm(request.POST)

            if customer_reg_form.is_valid():
                email = customer_reg_form.cleaned_data['customer_email']
                password = customer_reg_form.cleaned_data['customer_password']
                user = User.objects.create_user(email=email, password=password, username=email)
                user.save()
                customer_reg = customer_reg_form.save(commit=False)
                customer_reg.user = user
                customer_reg.save()
                return HttpResponseRedirect('/')
            else:
                return render(request, 'registration.html', {'customer_reg_form': customer_reg_form})
    else:
        customer_reg_form = CustomerRegForm()
        return render(request, 'registration.html', {'customer_reg_form': customer_reg_form})


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            msg = "نام کاربری یا کلمه عبور نامعتبر است."
            return render(request, 'login.html', {'login_form': login_form, 'msg': msg})
        else:
            return render(request, 'login.html', {'login_form': login_form})
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})
