from django import forms
from django.forms import ModelForm

from .models import Contact


class UserContact(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','subject','email',"message"]
    

    name = forms.CharField(error_messages={'required':"fill must be filed up !!"}, label='', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your name',

    }))
    email = forms.EmailField(label='', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Type your email',
        'type': 'email',
        'class': 'form-control',
    }))
    subject = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your subject',

    }))
    message = forms.CharField(label='', required=True, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                    'rows': 8,
                                                                                    'placeholder': 'Type your Message'
                                                                                    }
                                                                             ))

                                                                           

  
  