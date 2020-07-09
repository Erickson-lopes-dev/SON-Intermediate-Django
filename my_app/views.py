from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse


def login(request):
    if request.method == 'GET':
        return render(request, 'my_app/login.html')

    # Recebe as informações do formulário
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    # se for True
    if user:
        # criando sessão e cookie
        django_login(request, user)
        # redireciona a url
        return redirect('/home/')
    # mensagem que será exibida se as credenciais nao forem validas
    message = 'Credencias inválidas'

    # se caso esteja com informações inválida
    return render(request, 'my_app/login.html', {'message': message})


def home(request):
    return render(request, 'my_app/home.html')


def logout(request):
    # destroi a sessão
    django_logout(request)
    return render(request, 'my_app/login.html')
