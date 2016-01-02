from django.views.generic import FormView, View, TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.shortcuts import render

from user.forms import AdditionalInfoForm
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


# def additional_info(request):
#     if request.method == "POST":
#         additional_info_form = AdditionalInfo(request.POST)
#         if additional_info_form.is_valid():
#             pass
#
#         else:
#             return render(request, 'additional-info.html', {'additional_info_form': additional_info_form})
#
#     else:
#         additional_info_form = AdditionalInfo()
#         return render(request, 'additional-info.html',
#                       {'additional_info_form': additional_info_form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


class AdditionalInfo(FormView):
    template_name = 'additional-info.html'
    form_class = AdditionalInfoForm

    def form_valid(self, form):
        customer = form.save(commit=False)
        email = form.cleaned_data['email']
        customer.user = User.objects.get(email=email)
        customer.save()
        return redirect(reverse('user:additional_info'))


class ProfileCustomer(TemplateView):
    template_name = 'profile-customer.html'

    def get(self, request, *args, **kwargs):
        # customer_id = kwargs.pop('customer_id')
        return render(request, self.template_name, {})
