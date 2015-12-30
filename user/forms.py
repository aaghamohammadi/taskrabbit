from django import forms
from django.contrib.auth.models import User
from user.models import Customer


class CustomerRegForm(forms.ModelForm):
    customer_email = forms.EmailField(required=True, label='پست الکترونیک', widget=forms.TextInput(
        attrs={'placeholder': 'پست الکترونیک', 'class': 'required'}))
    customer_password = forms.CharField(required=True, label='کلمه عبور', widget=forms.PasswordInput(
        attrs={'placeholder': 'کلمه عبور', 'class': 'required'}))

    class Meta:
        model = Customer
        fields = ['customer_email', 'customer_password']

    def clean_customer_email(self):
        if (User.objects.filter(email=self.cleaned_data['customer_email'])).count() > 0:
            raise forms.ValidationError('پست الکترونیک انتخاب شده تکراری است.')

        return self.cleaned_data['customer_email']

    def clean_customer_password(self):
        if len(self.cleaned_data['customer_password']) < 6:
            raise forms.ValidationError('طول کلمه عبور باید حداقل ۴ کاراکتر باشد.')
        return self.cleaned_data['customer_password']

# class LoginForm(forms.ModelForm):
#     email = forms.EmailField(required=True, label='پست الکترونیک ')
#     password = forms.CharField(required=True, label='رمز عبور', widget=forms.PasswordInput)
