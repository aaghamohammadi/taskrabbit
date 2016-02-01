from django import forms
from review.models import Comment, Rate


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', ]
        widgets = {
            'context': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'comment_set': forms.HiddenInput()
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude = ['customer', 'order']
        widgets = {
            'rate': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '10'}),
        }
