from django import forms
import re
from django.contrib.auth.models import User
from django.core.validators import validate_email, RegexValidator
from socialnetwork.models import *

class RegistrationForm(forms.Form):
    username   = forms.CharField(max_length = 20,
                                 widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    password1  = forms.CharField(max_length = 200, 
                                 label='Password', 
                                 widget = forms.PasswordInput(attrs={'class' : 'myfieldclass'}))
    password2  = forms.CharField(max_length = 200, 
                                 label='Confirm password',  
                                 widget = forms.PasswordInput(attrs={'class' : 'myfieldclass'}))

    email      = forms.CharField(max_length = 40,
                                 validators = [validate_email],
                                 widget = forms.TextInput(attrs={'class' : 'myfieldclass'}))

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(RegistrationForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data


    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username



class messageform(forms.ModelForm):
    class Meta:
        model=Item
        exclude=('user','date','username',)

class profileform(forms.ModelForm):
    class Meta:
        model=profile
        exclude=('user','username','picture')
        widgets={'firstname':forms.TextInput(attrs={'class' : 'myfieldclass'}),
                 'lastname':forms.TextInput(attrs={'class' : 'myfieldclass'}),
                 'age':forms.TextInput(attrs={'class' : 'myfieldclass'}),
                 'short_bio':forms.TextInput(attrs={'class' : 'myfieldclass'}),}
    pic = forms.FileField(required=False)




