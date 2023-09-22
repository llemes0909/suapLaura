from django.shortcuts import render
from . models import*

def pessoa(request):
    pessoas = {
        'pessoas':Pessoa.objects.all()
        }
    return render(request, 'pessoas/pessoas.html', pessoas)

