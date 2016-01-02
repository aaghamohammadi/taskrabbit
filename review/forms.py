from django import forms
from review.models import Comment, Rating


class CommentForm(forms.ModelForm):
    # goh = forms.IntegerField()

    class Meta:
        model = Comment
        exclude = ['customer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'required'}),
            'context': forms.Textarea(attrs={'class': 'materialize-textarea'})
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['customer', 'tasker']
        widgets = {
            'kindness': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '5'}),
            'price': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '5'}),
            'performance': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '5'}),
            'speed': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '5'}),

        }
