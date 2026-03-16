from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none',
        'placeholder': 'seu@email.com'
    }))
    username = forms.CharField(label='Nome', widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none',
        'placeholder': 'Seu Nome'
    }))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none',
        'placeholder': '••••••••'
    }))
    termos = forms.BooleanField(required=True, label='Aceito os Termos de Uso e Política de Privacidade', widget=forms.CheckboxInput(attrs={
        'class': 'w-4 h-4 text-primary border-slate-300 rounded focus:ring-primary'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email ou Nome', widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none',
        'placeholder': 'Email ou Nome'
    }))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none',
        'placeholder': '••••••••'
    }))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'telefone', 'cidade', 'estado', 'bio', 'foto', 'facebook', 'instagram']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50'}),
            'telefone': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50', 'placeholder': '(11) 99999-9999'}),
            'cidade': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50'}),
            'estado': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50', 'placeholder': 'SP'}),
            'bio': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50', 'rows': 4}),
            'facebook': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50', 'placeholder': 'facebook.com/seuusuario'}),
            'instagram': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50', 'placeholder': '@seuusuario'}),
        }
