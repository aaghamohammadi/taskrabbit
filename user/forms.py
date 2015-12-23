from django import forms
from user.models import Person


class PersonRegModelForm(forms.ModelForm):
    person_email = forms.EmailField(required=True, label='پست الکترونیک', widget=forms.TextInput(
        attrs={'placeholder': ' مثال: aghamohammadi@taskrabbit.ir', 'class': 'required'}))
    person_password = forms.CharField(required=True, label='???? ????')

    class Meta:
        model = Person

    def clean_person_email(self):
        if (Person.objects.filter(email=self.cleaned_data['person_email'])).count() > 0:
            raise forms.ValidationError('پست الکترونیک انتخاب شده تکراری است.')

        return self.cleaned_data['person_email']

    def clean_person_password(self):
        if len(self.cleaned_data['person_email']) < 6:
            raise forms.ValidationError('رمز عبور باید حداقل ۶ نویسه باشد')


class LoginForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='پست الکترونیک ')
    password = forms.CharField(required=True, label='رمز عبور', widget=forms.PasswordInput)
