from django import forms
from django.contrib.auth.models import User

# from user.models import Customer, Date
from user.models import Member

GENDER_CHOICES = (
    ('M', 'مرد'),
    ('F', 'زن'),
)

TIME_CHOICES = (
    ('morning', 'صبح'),
    ('noon', 'ظهر'),
    ('afternoon', 'بعد از ظهر'),
    ('full time', 'تمام وقت')
)


class CustomerRegForm(forms.ModelForm):
    member_email = forms.EmailField(required=True, label='پست الکترونیک', widget=forms.TextInput(
            attrs={'class': 'required'}))
    member_password = forms.CharField(required=True, label='کلمه عبور', widget=forms.PasswordInput(
            attrs={'class': 'required'}))
    gender = forms.ChoiceField(required=False, label='جنسیت',
                               widget=forms.RadioSelect(attrs={'id': 'gender', 'type': 'radio'}),
                               choices=GENDER_CHOICES)

    class Meta:
        model = Member
        fields = ['full_name', 'member_email', 'member_password', 'mobile_number', 'gender', 'city', 'address']
        labels = {
            'full_name': 'نام کامل',
            'mobile_number': 'شماره تلفن همراه',
            'city': 'شهر',
            'address': 'آدرس'
        }
        widgets = {
            'full_name': forms.TextInput(),
            'mobile_number': forms.TextInput(attrs={'type': 'number'})
        }

    def clean_member_email(self):
        if (User.objects.filter(email=self.cleaned_data['member_email'])).count() > 0:
            raise forms.ValidationError('پست الکترونیک انتخاب شده تکراری است.')

        return self.cleaned_data['member_email']

    def clean_member_password(self):
        if len(self.cleaned_data['member_password']) < 4:
            raise forms.ValidationError('طول کلمه عبور باید حداقل ۴ کاراکتر باشد.')
        return self.cleaned_data['member_password']


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='نام کامل', widget=forms.TextInput(
            attrs={'placeholder': 'نام کامل', 'class': 'required'}))
    password = forms.CharField(required=True, label='رمز عبور', widget=forms.PasswordInput(
            attrs={'placeholder': 'کلمه عبور', 'class': 'required'}))


class EditCustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['mobile_number', 'city', 'address', 'image']

        labels = {
            'mobile_number': 'شماره تلفن همراه',
            'city': 'شهر',
            'address': 'آدرس',
            'image': 'عکس'
        }


class SearchForm(forms.Form):
    skill_name = forms.CharField(max_length=50, required=False, label='نام مهارت')
    city = forms.CharField(max_length=50, required=False, label='شهر')
    location = forms.CharField(max_length=50, required=False, label='آدرس')
    max_price = forms.IntegerField(required=False, label='حداکثر قیمت')
    min_rate = forms.IntegerField(required=False, label='حداقل امتیاز')

    def clean_max_price(self):
        if not self.cleaned_data['max_price']:
            return (1 << 31) - 1
        else:
            return self.cleaned_data['max_price']

    def clean_min_rate(self):
        if not self.cleaned_data['min_rate']:
            return 0
        else:
            return self.cleaned_data['min_rate']
