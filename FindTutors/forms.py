from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TUser, Profile
from django.forms import ModelForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms import bootstrap
from django.utils.translation import gettext_lazy as _


# Creating a Central Registration Form that will work for both Tutor and Tutee (set Booleans in view)


class RegisterForm(UserCreationForm):
    def __init__(self, data=None, files=None, request=None, recipient_list=None, *args, **kwargs):
        super().__init__(data=data, files=files, request=request, recipient_list=recipient_list,
                         *args, **kwargs)
        self.fields['firstname'].widget.attrs['placeholder'] = 'name'
        self.fields['email'].widget.attrs['placeholder'] = 'e-mail'
        self.fields['body'].widget.attrs['placeholder'] = 'message'

    class Meta:
        model = TUser
        fields = ['username', 'firstname', 'lastname',
                  'email', 'phone_number', 'subjects', 'year']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'subjects': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'year': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class TutorUserSignUpForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email',
                  'phone_number', 'year', 'subjects')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = "font-weight-light"
        self.helper.layout = Layout(
            Field(
                'firstname',
                wrapper_class="md-form",
            ),
            Field('lastname', wrapper_class="md-form"),
            Field('email', wrapper_class="md-form"),
            Field('phone_number', wrapper_class="md-form"),
            Field('year', wrapper_class="md-form"),
            Field('subjects', wrapper_class="md-form"),
            Submit('submit', ' Register As Tutor!')

        )


class TuteeUserSignUpForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email',
                  'phone_number', 'year', 'subjects')


# TutorRegistrationForm
class TutorRegistration(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'phone_number', 'subjects')


# update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'year', 'user_type', 'subjects', 'bio']
