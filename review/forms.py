from django import forms
from review.models import Comment, Rating


class CommentForm(forms.ModelForm):
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
            'rating': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '10'}),
        }
