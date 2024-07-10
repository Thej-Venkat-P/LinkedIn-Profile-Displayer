from django import forms

class ProfileForm(forms.Form):
    url = forms.CharField(label='LinkedIn Profile URL', max_length=100)
