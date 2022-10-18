from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, user_logged_out
from django.contrib.auth.models import User


from .models import User
from .forms import RegisForm, LoginForm

# Create your views here.

def regisPage(req):
    # if req.user.is_authenticated:
    #     return redirect('/')
    # else:
    form = RegisForm()
    if req.POST:
        form = RegisForm(req.POST)
        # if form.is_valid(instance=form.jurusan):
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            HttpResponse('Uername atau Password Anda Salah, mohon ulang registrasi')
    return render(req, 'account/register.html', {'form':form,})

def loginPage(req):
    form = LoginForm(req.POST)
    msg = None
    if req.POST:
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_panitia:
                login(req, user)
                # sessionUser = req.session["jurusan"]  = user.jurusan
                # print(sessionUser)
                return redirect('/panitia')
            elif user is not None and user.is_pemilih:
                login(req, user)
                return redirect('/pemilih')
            else:
                form = LoginForm()
        else:
            form = LoginForm()
    return render(req, 'account/login.html', {
        'form': form,
        'msg':msg,
    })

def logoutPage(req):
    logout(req)
    return redirect('/')
    # user = getattr(req, 'user', None)
    # if hasattr(user, 'is_authenticated') and not user.is_authenticated():
    #     user = None
    # user_logged_out.send(sender=user.__class__, req=req, user=user)

    # req.session.flush()
    # if hasattr(req, 'user'):
    #     from django.contrib.auth.models import AnonymousUser
    #     req.user = AnonymousUser()


# ====================================

# def registerPage(req):
#     form = RegisForm()
#     if req.POST:
#         form = RegisForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             form = RegisForm()
#     return render(req, 'register.html', {'form':form})

# def loginPage(req):
#     form = LoginForm(req.POST or None)
#     if req.POST:
#         username = req.POST.get('username')
#         password = req.POST.get('password')
#         user = authenticate(req, username=username, password=password)

#         if user is not None and user.is_panitia:
#             login(req, user)
#             if user.check_password(req.POST['password']):
#                 req.session['username']=username
#                 return redirect('/panitia')
#             else:
#                 return redirect('/')
#         elif user is not None and user.is_pemilih:
#             login(req, user)
#             if user.check_password(req.POST['password']):
#                 req.session['username']=username
#                 return redirect('/pemilih')
#             else:
#                 return redirect('/')
#         else:
#             return redirect('/')
#     return render(req, 'login.html', {'form':form})

# def logoutPage(request):
#     try:
#         del request.session['user']
#     except:
#         return redirect('login')
#     return redirect('login')