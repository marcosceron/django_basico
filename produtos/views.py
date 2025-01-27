from django.shortcuts import render
from django.http import HttpResponse
from .models import ProdutoFinal

from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login/")
def ver_produto(request):
    produtos_finais = {
        'produtos_finais': ProdutoFinal.objects.all()
    }


    return render(request, 'produtos/ver_produto.html', produtos_finais)

def inserir_produto(request):
    return HttpResponse('Estou no inserir')