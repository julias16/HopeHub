import re
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

User = get_user_model()
phone_regex = RegexValidator(regex=r'^\+?\d{7,15}$', message='Enter a valid phone number (7-15 digits, optional leading +).')

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'phone', 'address')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Email already in use.')
        return email.lower()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError('Username already in use.')
        return username

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise ValidationError('Phone is required.')
        phone = phone.strip()
        phone_regex(phone)
        normalized = re.sub(r'\D', '', phone)
        if User.objects.filter(phone__iexact=normalized).exists():
            raise ValidationError('Phone already in use.')
        return normalized

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError({'password2': "Passwords do not match."})
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    identifier = forms.CharField(label='Username / Email / Phone')
    password = forms.CharField(widget=forms.PasswordInput)
