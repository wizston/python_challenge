from django import forms


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, help_text='100 characters max')
    email = forms.EmailField(required=True)

