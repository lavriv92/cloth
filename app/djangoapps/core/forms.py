from django import forms
from django.core import validators
from django.core.mail import send_mail


class ContactForm(forms.Form):
    """
    Contact form
    """
    name = forms.CharField(validators=[validators.MinLengthValidator(6)])
    email = forms.EmailField()
    body = forms.CharField(validators=[validators.MinLengthValidator(20)])

    def send_mail(self):
        """
        Send contact mail
        """
        email = self.cleaned_data.get('email')
        name = self.cleaned_data.get('name')
        body = self.cleaned_data.get('body')
        message = '{0}. by {1}'.format(body, name)
        send_mail('Contact form', message, email, ['lavriv92@gmail.com'])
