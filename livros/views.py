from django.shortcuts import render

def listar_livros(request):
    return render(request, 'livros/listar.html')