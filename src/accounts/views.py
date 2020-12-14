from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    elif request.method == 'POST':
        print(request.POST)
        return redirect('auth/')
    
def autentication(request):
    print(request.POST)
    #user = authenticate(username=request.POST['nome'], password=request.POST['email'])
    return render(request, 'store/store.html')