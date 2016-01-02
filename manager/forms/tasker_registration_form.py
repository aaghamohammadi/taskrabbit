from django import forms

from user.models import Customer


__author__ = 'garfild'

GENDER_CHOICES = (
    ('M', 'مرد'),
    ('F', 'زن'),
)


class TaskerRegistrationForm(forms.ModelForm):
    gender = forms.ChoiceField(required=False, label='جنسیت',
                               widget=forms.RadioSelect(attrs={'id': 'person', 'type': 'radio'}),
                               choices=GENDER_CHOICES)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'national_id', 'home_number', 'mobile_number', 'birthday', 'gender',
                  'city',
                  'district']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'national_id': 'کد ملی',
            'home_number': 'شماره تلفن ثابت',
            'mobile_number': 'شماره تلفن همراه',
            'birthday': 'تاریخ تولد',
            'city': 'شهر',
            'district': 'محله'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'مثال: علیرضا'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'مثال: آقامحمدی'}),
            'national_id': forms.TextInput(attrs={'type': 'number', 'placeholder': 'مثال: ۰۰۱۶۴۹۹۸۰۸'}),
            'home_number': forms.TextInput(attrs={'type': 'number', 'placeholder': 'مثال: ۰۲۱۴۴۶۶۲۳۶۸'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'مثال: ۰۹۱۲۶۰۲۷۷۸۳'}),
            'birthday': forms.TextInput(attrs={'class': 'datepicker'})
        }
