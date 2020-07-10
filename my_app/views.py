from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Adress, STATES_CHOICES
from .forms import AddressForm


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
    form_submitted = False
    if request.method == 'GET':
        # state = STATES_CHOICES
        form = AddressForm()

    else:
        form_submitted = True
        form = AddressForm(request.POST)
        if form.is_valid():
            Adress.objects.create(
                address=form.cleaned_data['address'],
                address_complement=form.cleaned_data['address_complement'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                country=form.cleaned_data['country'],
                user=request.user
            )
        return redirect('/addresses/')

    return render(request, 'my_app/address/create.html', {'form': form, 'form_submitted': form_submitted})


@login_required(login_url='/login/')
def address_upate(request, id):
    form_submitted = False
    address = Adress.objects.get(id=id)
    if request.method == 'GET':
        # state = STATES_CHOICES
        form = AddressForm(address.__dict__)
    else:
        form_submitted = True
        address.address = request.POST.get('address')
        address.address_complement = request.POST.get('address_complement')
        address.city = request.POST.get('city')
        address.state = request.POST.get('state')
        address.country = request.POST.get('country')

        address.save()
        return redirect('/addresses/')

    return render(request, 'my_app/address/update.html', {'form': form,
                                                          'address': address,
                                                          'form_submitted': form_submitted})
