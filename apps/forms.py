from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, Form

from apps.models import User


# class RegisterForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

class RegisterForm(ModelForm):
    confirm_password = CharField(max_length=255)
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')

    def clean_password(self):
        if self.cleaned_data['password'] != self.data['confirm_password']:
            raise ValidationError('Password didn\'t match ')
        return make_password(self.cleaned_data['password'])


class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['password', 'email', 'city', 'state', 'street', 'username', 'first_name', 'job', 'image', 'about_me', 'zip_code']

    def clean_password(self):
        # self.password = make_password(self.password)
        return make_password(self.cleaned_data['password'])


class CustomLoginForm(AuthenticationForm):
    pass