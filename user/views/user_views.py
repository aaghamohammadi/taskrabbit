import hashlib
import datetime
import random

from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

from django.shortcuts import render
from review.forms import CommentForm, RatingForm

from user.forms import AdditionalInfoForm, TaskerAvailabilityForm
from user.forms import CustomerRegForm, LoginForm
from user.models import Member


def index(request):
    return render(request, 'index.html', {})


def registration(request):
    if request.method == "POST":
        if 'member-reg-btn' in request.POST:
            customer_reg_form = CustomerRegForm(request.POST)

            if customer_reg_form.is_valid():
                # email = customer_reg_form.cleaned_data['member_email']
                # password = customer_reg_form.cleaned_data['member_password']
                # username = customer_reg_form.cleaned_data['full_name']
                # user = User.objects.create_user(email=email, password=password, username=username)
                # user.save()
                # customer_reg = customer_reg_form.save(commit=False)
                # customer_reg.user = user
                # customer_reg.save()
                # return HttpResponseRedirect('/')
                username = customer_reg_form.cleaned_data['full_name']
                email = customer_reg_form.cleaned_data['member_email']
                password = customer_reg_form.cleaned_data['member_password']

                mobile_number = customer_reg_form.cleaned_data['mobile_number']
                gender = customer_reg_form.cleaned_data['gender']
                city = customer_reg_form.cleaned_data['city']
                address = customer_reg_form.cleaned_data['address']

                user = User.objects.create_user(email=email, password=password, username=username)
                user.is_active = False
                user.save()
                logout(request)

                salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
                activation_key = hashlib.sha1((salt + email).encode('utf-8')).hexdigest()
                key_expires = datetime.datetime.today() + datetime.timedelta(2)

                new_member = Member(user=user, activation_key=activation_key, key_expires=key_expires,
                                    mobile_number=mobile_number, gender=gender, city=city, address=address,
                                    full_name=username)
                new_member.save()

                # send email
                email_subject = 'تأیید حساب کاربری'
                email_body = "سلام %s,\n" \
                             "با تشکر از شما بابت ثبت نام در سایت خدمت گزار، لطفا از طریق لینک زیر تا ۴۸ ساعت " \
                             "آینده حساب کاربری خود را فعال نمایید.\n\
                           http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)

                send_mail(email_subject, email_body, 'aaghamohammadi@ce.sharif.edu',
                          [email], fail_silently=False)
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
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
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


def register_confirm(request, activation_key):
    if request.user.is_authenticated():
        HttpResponseRedirect('/')

    user_member = get_object_or_404(Member, activation_key=activation_key)

    if user_member.key_expires < datetime.datetime.now():
        return render_to_response('confirm_expired.html')

    user = user_member.user
    user.is_active = True
    user.save()
    return render_to_response('confirm.html')


def profile_user(request, customer_id):
    template_name = 'profile-customer.html'
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        rating_form = RatingForm(request.POST)

    else:
        comment_form = CommentForm()
        rating_form = RatingForm()
        return render(request, template_name,
                      {'member': member, 'comment_form': comment_form, 'rating_form': rating_form})


class AdditionalInfo(FormView):
    template_name = 'additional-info.html'
    form_class = AdditionalInfoForm

    def form_valid(self, form):
        customer = form.save(commit=False)
        email = form.cleaned_data['email']
        customer.user = User.objects.get(email=email)
        customer.save()
        return redirect(reverse('user:additional_info'))


class ProfileTakser(TemplateView):
    template_name = 'profile-tasker.html'

    def get(self, request, *args, **kwargs):
        availability_form = TaskerAvailabilityForm()
        return render(request, self.template_name, {'availability_form': availability_form})


class Work(TemplateView):
    template_name = 'work.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

# class ProfileCustomer(FormView):
#     template_name = 'profile-customer.html'
#     model = Member
#
#     def get(self, request, *args, **kwargs):
#         # customer_id = kwargs.pop('customer_id')
#         comment_form = CommentForm()
#         rating_form = RatingForm()
#         return render(request, self.template_name, {'comment_form': comment_form,
#                                                     'rating_form': rating_form})
