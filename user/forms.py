from django import forms

class UserForm(forms.Form):
    firstName = forms.CharField(max_length=255)
    lastName = forms.CharField(max_length=255)
    email = forms.EmailField()
