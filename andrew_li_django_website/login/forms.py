from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'captcha'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data('username')
        user.email = self.cleaned_data('email')

        if commit:
            user.save()

        return user
