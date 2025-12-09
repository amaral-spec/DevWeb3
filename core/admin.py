from django.contrib import admin
from .models import Autor, Categoria, Livro, Emprestimo, Perfil

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nacionalidade']
    search_fields = ['nome']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'disponivel', 'quantidade']
    list_filter = ['disponivel', 'categoria', 'autor']
    search_fields = ['titulo', 'autor__nome', 'isbn']
    list_editable = ['disponivel', 'quantidade']

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['livro', 'usuario', 'data_emprestimo', 'data_devolucao', 'status']
    list_filter = ['status', 'data_emprestimo']
    search_fields = ['livro__titulo', 'usuario__username']

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['user', 'telefone']
    search_fields = ['user__username']