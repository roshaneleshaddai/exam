from django import forms

class SignupForm(forms.Form):
    username_or_mobile = forms.CharField(label='Username_or_mobile', max_length=30)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    