from django import forms
from .models import Profile

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': 'Имя пользователя',
        'class': 'form-control'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': 'form-control'
    }))

    error_messages = {
        'invalid_login': 'Введен неверный пароль'
    }


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label= 'Пароль',
        widget= forms.widgets.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }))

    password2 = forms.CharField(
        label = 'Повторите пароль',
        widget = forms.widgets.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
            'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Email'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=User).exists():
            raise forms.ValidationError('Email addresses must be unique')
        return email


class UpdateProfileForm(forms.ModelForm):
    max_size_img = 3
    date_birth = forms.DateField(label='Дата рождения', 
        input_formats=['%d-%m-%Y'],
        widget= forms.DateInput(format=('%d-%m-%Y'), attrs={
        'class': 'form-control',
        'placeholder': 'Дата рождения'
        })
    )

    class Meta:
        model = Profile
        fields = ['date_birth', 'about', 'avatar']
        label = {
            'about': 'Обо мне ',
            'avatar':'Фото профиля'
        }
        widgets = {
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Обо мне'}),
        }
    
    def clean_avatar(self):
        image = self.cleaned_data.get('avatar', False)
        if image:
            if image.size > self.max_size_img*1024*1024:
                raise forms.ValidationError(f'Файл должен быть не больше {self.max_size_img} мб')
            return image

        else:
            raise forms.ValidationError('Не удалось прочитать файл')