from django import forms
from .models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email',)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'email',
        'type': 'email',
        'name': 'EMAIL',
        'id': 'mc-email',
        'placeholder': 'Email Address'
    }), label='')


class ContactForm(forms.Form):
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
        'class': 'full-width message',
        'name': 'cMessage',
        'id': 'cMessage',
        'placeholder': 'Your Message',
        'type': 'text'
    }), label='')
