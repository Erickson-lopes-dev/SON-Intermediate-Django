from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Adress, STATES_CHOICES

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

    # # fazer algo quando o usuario estiver autenticado
    # if request.user.is_authenticated():
    # request.user.first_name


@login_required(login_url='/login/')
def home(request):
    return render(request, 'my_app/home.html')


@login_required(login_url='/login/')
def logout(request):
    # destroi a sessão
    django_logout(request)
    return render(request, 'my_app/login.html')


@login_required(login_url='/login/')
def address_list(request):
    addresses = Adress.objects.all()
    return render(request, 'my_app/address/list.html', {'addresses': addresses})


@login_required(login_url='/login/')
def address_create(request):
    if request.method == 'GET':
        state = STATES_CHOICES
        return render(request, 'my_app/address/create.html', {'states': state})

    Adress.objects.create(
        address=request.POST.get('address'),
        address_complement=request.POST.get('address_complement'),
        city=request.POST.get('city'),
        state=request.POST.get('state'),
        country=request.POST.get('country'),
        user=request.user
    )
    return redirect('/addresses/')