from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    args = {}
    texto = 'index'
    args['titulo'] = texto
    return render(request, "index.html", args)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect(index,{'titulo':'Login'})
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(index,{'titulo':'Login'})
            else:
                messages.info(request, 'Usuario y/o contraseña incorrecto')
        return render(request, "login.html", {'titulo':'Login'})