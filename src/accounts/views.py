from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')

    elif request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']

        user = authenticate(request, username=name, password=email)
        if user is not None:
            auth_login(request, user)
        return redirect('auth/')
