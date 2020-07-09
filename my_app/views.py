from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse


def login(request):
    if request.method == 'GET':
        return render(request, 'my_app/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    # se for True
    if user:
        return HttpResponse('Credenciais validas')
    return HttpResponse('Credenciais inválidas')
