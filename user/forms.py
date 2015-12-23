from django import forms
from user.models import Person


class PersonRegModelForm(forms.ModelForm):
    person_email = forms.EmailField(required=True, label='??? ?????????', widget=forms.TextInput(
        attrs={'placeholder': ' ????: mozhpar@gisheh.ir', 'class': 'required'}))
    person_password = forms.CharField(required=True, label='???? ????')

    class Meta:
        model = Person

    def clean_person_email(self):
        if (Person.objects.filter(email=self.cleaned_data['person_email'])).count() > 0:
            raise forms.ValidationError('??? ????????? ?????? ??? ?????? ???.')

        return self.cleaned_data['person_email']

    def clean_person_password(self):
        if len(self.cleaned_data['person_email']) < 6:
            raise forms.ValidationError('??? ???? ???? ????? ? ????? ????.')


class LoginForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='??? ?????????')
    password = forms.CharField(required=True, label='???? ????', widget=forms.PasswordInput)
