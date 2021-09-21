from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150,required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email__iexact = email)

        if query.exists():
            raise forms.ValidationError('That Email is already taken. Please choose another!')
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')   
        if username and password:
            
            query = User.objects.filter(username__iexact = username)
            if not query.exists():
                self.add_error('username','The user does not exist')
            else:
                is_active_query = User.objects.filter(username__iexact = username, is_active=True)
                if not is_active_query.exists():
                    print('Account is not active, your need to activate your account before login. An account activation link has been sent to your mailbox')                
                else:
                    user = authenticate(username=username, password=password)  
                    if not user:
                        self.add_error('password',"Incorrect password. Please try again!")
        return super(UserLoginForm, self).clean(*args, **kwargs)
    