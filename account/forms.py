from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisForm(UserCreationForm):
    JURUSAN = [
        (1,'Informatika'),
        (2, 'Teknik Komputer'),
        (3, 'Teknik Elektro'),
        (4, 'Studi Islam Interdisipliner'),
        (5, 'Agribisnis'),
        (6, 'Farmasi'),
        (7, 'Pendidikan Guru Sekolah Dasar'),
        (8, 'Pendidikan Bahasa Inggris'),
        (9, 'Menejemen'),
        (10, 'Akuntansi'),
        (11, 'Teknologi Hasil Pertanian'),
    ]
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'konfirmasi password'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}))
    jurusan = forms.CharField(widget=forms.Select(choices=JURUSAN))
    
    class Meta:
        model = User
        fields = ['jurusan', 'username', 'email', 'password1', 'password2', 'is_panitia', 'is_pemilih']

