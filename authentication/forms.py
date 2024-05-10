# authentication/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .import validators

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='User Name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'User Name'}))
    password = forms.CharField(max_length=63,label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')
    

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        validator = validators.ContainsLetterValidator()
        try:
            validator.validate(password1)
            print(validator.validate(password1))
        except forms.ValidationError as e:
            self.add_error('password1', e)
        return password1