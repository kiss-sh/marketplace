from django.shortcuts import render
from django.contrib.auth import authenticate

def login(request):

    print(asdddddddddddddddddddddddddd)
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    elif request.method == 'POST':
        print(request.POST)
        return render(request, 'registration/login.html')

def autentication(request):

    print(request.POST)
    """
    user = authenticate(username=None, password=None)
    if user is not None:
        pass
    else:
        pass
    """
