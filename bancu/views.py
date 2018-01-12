from django.shortcuts import render
from django.http import HttpResponse
from .forms import SaqueForm

def hello(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print(request.POST)
        form = SaqueForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            contexto = form.data
            print(contexto)
            print("O valor é: ", contexto['valor'])

    saldo_caixa = 100
    return render(request, 'index.html', {'form': SaqueForm})

def saque(request):
    saldo_caixa = 100
    return render(request, 'index.html', {'form': SaqueForm})


