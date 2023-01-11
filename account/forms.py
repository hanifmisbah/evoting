from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    # class Meta:
    #     fields = '__all__'
    #     labels = {
    #         'username':'Username',
    #         'password':'Password',
    #     }
    

class RegisForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = [
            'jurusan',
            'first_name',
            'nim',
            'email',
            'no_wa',
            'username',
            'password1',
            'password2',
            'is_panitia',
            'is_pemilih'
        ]
        labels = {
            'jurusan': 'Jurusan',
            'first_name': 'Nama Lengkap',
            'nim':'Nomor Induk Mahasiswa',
            'email':'Email',
            'no_wa':'Nomor Telp',
            'username':'Username',
            'password1':'Password',
            'password2':'Konfirmasi Password',
            'is_panitia':'Panitia',
            'is_pemilih':'Pemilih'
        }

