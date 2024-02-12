from django.shortcuts import render
from .models import Cliente

def home(request):
    return render(request, 'clientes/home.html')

def clientes(request):
    #salvar os dados da tela no db
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.cpf = request.POST.get('cpf')
    novo_cliente.telefone = request.POST.get('telefone')
    novo_cliente.save()

    #exibir todos os clientes cadastrados em uma nova página
    clientes = {
        'clientes': Cliente.objects.all()
    }     

    #retornar os dados para a página de listagem de clientes
    return render(request, 'clientes/clientes.html', clientes)





    clientes = {'clientes': Cliente.objects.all()}
    return render(request, 'clientes/clientes.html', clientes)
