from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'full-width',
        'name': 'cName',
        'id': 'cName',
        'placeholder': 'Your Name',
        'type': 'text'
    }), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'full-width',
        'name': 'cEmail',
        'id': 'cEmail',
        'placeholder': 'Your Email',
        'type': 'text'
    }), label='')
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'message full-width',
        'name': 'cMessage',
        'id': 'cMessage',
        'placeholder': 'Your Message',
    }), label='')
