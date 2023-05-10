from django.shortcuts import render

# Create your views here.
def index(request):
    meu_nome = 'Beltrano da Costa'
    lista_frutas = ['laranja', 'maça', 'banana']
    context = {
        'nome' : meu_nome,
        'frutas' : lista_frutas
        }
    return render(request, 'index.html', context)

def listar_clientes(request):
    return render(request, 'lista_cliente.html')