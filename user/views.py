from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from user.forms import CustomerRegForm


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
                customer_reg_form = CustomerRegForm()
                return render(request, 'registration.html', {'customer_reg_form': customer_reg_form})
    else:
        customer_reg_form = CustomerRegForm()
        return render(request, 'registration.html', {'customer_reg_form': customer_reg_form})
