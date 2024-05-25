from django.shortcuts import render
from django import forms

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

#password Change
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SignUpView(CreateView):
    form_class = SignUpForm
    # form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            # If the email is already registered, raise a validation error
            raise ValidationError("This email is already registered.")
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add an email field to the form
        form.fields['email'].required = True
        return form



class ChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')


class ChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'