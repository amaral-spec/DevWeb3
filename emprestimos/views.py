from django.shortcuts import render

def listar_emprestimos(request):
    return render(request, 'emprestimos/listar.html')