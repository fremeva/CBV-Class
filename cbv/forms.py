from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ExampleForm(forms.Form):
    test = forms.CharField(max_length=10)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ExampleForm, self).__init__(*args, **kwargs)


class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(UserModelForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserModelForm, self).clean()

        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError("The password fields are not equal")

    def clean_username(self):
        if self.cleaned_data['username'] == "test":
            raise ValidationError("I Dont want tests users")
        return self.cleaned_data['username']