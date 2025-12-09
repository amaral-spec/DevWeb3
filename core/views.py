from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Livro, Autor, Categoria, Emprestimo
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def home(request):
    """Página inicial"""
    livros = Livro.objects.filter(disponivel=True)[:6]
    total_livros = Livro.objects.count()
    total_autores = Autor.objects.count()
    
    context = {
        'livros': livros,
        'total_livros': total_livros,
        'total_autores': total_autores,
    }
    return render(request, 'core/home.html', context)

def sobre(request):
    """Página sobre o sistema"""
    return render(request, 'core/sobre.html')

def registro(request):
    """Registro de novos usuários"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'core/registro.html', {'form': form})

@login_required
def perfil(request):
    """Perfil do usuário"""
    return render(request, 'core/perfil.html')

# CRUD para Livros
@login_required
def listar_livros(request):
    """Lista todos os livros"""
    livros = Livro.objects.all()
    return render(request, 'core/livros/listar.html', {'livros': livros})

@login_required
def detalhar_livro(request, livro_id):
    """Detalhes de um livro"""
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, 'core/livros/detalhar.html', {'livro': livro})

@login_required
def adicionar_livro(request):
    """Adicionar novo livro (simplificado)"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor_id = request.POST.get('autor')
        
        if titulo and autor_id:
            Livro.objects.create(
                titulo=titulo,
                autor_id=autor_id,
                editora=request.POST.get('editora', ''),
                ano_publicacao=request.POST.get('ano_publicacao', 2024),
                quantidade=request.POST.get('quantidade', 1),
                disponivel=True
            )
            messages.success(request, 'Livro adicionado com sucesso!')
            return redirect('listar_livros')
    
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'core/livros/adicionar.html', {
        'autores': autores,
        'categorias': categorias
    })

@login_required
def editar_livro(request, livro_id):
    """Editar livro existente"""
    livro = get_object_or_404(Livro, id=livro_id)
    
    if request.method == 'POST':
        livro.titulo = request.POST.get('titulo', livro.titulo)
        livro.editora = request.POST.get('editora', livro.editora)
        livro.ano_publicacao = request.POST.get('ano_publicacao', livro.ano_publicacao)
        livro.quantidade = request.POST.get('quantidade', livro.quantidade)
        livro.disponivel = request.POST.get('disponivel') == 'on'
        livro.save()
        
        messages.success(request, 'Livro atualizado com sucesso!')
        return redirect('detalhar_livro', livro_id=livro.id)
    
    autores = Autor.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'core/livros/editar.html', {
        'livro': livro,
        'autores': autores,
        'categorias': categorias
    })

@login_required
def excluir_livro(request, livro_id):
    """Excluir livro"""
    livro = get_object_or_404(Livro, id=livro_id)
    
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('listar_livros')
    
    return render(request, 'core/livros/excluir.html', {'livro': livro})

def custom_logout(request):
    """Logout personalizado que funciona com GET"""
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.success(request, f'Até logo, {username}! Você foi desconectado.')
    
    # Redireciona para home
    return redirect('home')