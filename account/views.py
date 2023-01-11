from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from .models import User
from .forms import RegisForm, LoginForm

# Create your views here.

def regisPage(req):
    if req.user.is_authenticated:
        return redirect('/')
    else:
        form = RegisForm()
        if req.POST:
            form = RegisForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                HttpResponse('Uername atau Password Anda Salah, mohon ulang registrasi')
        return render(req, 'account/register.html', {'form':form,})

def loginPage(req):
    if req.user.is_authenticated:
        return redirect('/')
    else:
        form = LoginForm(req.POST)
        msg = None
        if req.POST:
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                
                if user is not None and user.is_panitia:
                    login(req, user)
                    req.session["user"]  = user.toDict()
                    return redirect('/panitia')
                elif user is not None and user.is_pemilih:
                    login(req, user)
                    req.session["user"]  = user.toDict()
                    return redirect('/pemilih')
                else:
                    return redirect('/')
                    # form = LoginForm()
            else:
                return redirect('/')
        return render(req, 'account/login.html', {
            'form': form,
            'msg':msg,
        })


def loginPageAdmin(req):
    form = LoginForm(req.POST)
    msg = None
    if req.POST:
        if form.is_valid():
            username=('admin1', 'admin2')
            # password=form.cleaned_data.get('password')
            user = authenticate(username=username, password='adminku123')
            
            if user is not None:
                login(req, user)
                return redirect('/superadmin')
            else:
                return redirect('/')
                # form = LoginForm()
        else:
            return redirect('/superadmi')
    return render(req, 'account/loginAdmin.html', {
        'form': form,
        'msg':msg,
    })
    

def logoutPage(req):
    logout(req)
    return redirect('/')
