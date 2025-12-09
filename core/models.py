from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    biografia = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nome']

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField(default=1)
    disponivel = models.BooleanField(default=True)
    sinopse = models.TextField(blank=True)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor.nome}"
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ['titulo']
    
    def estoque_disponivel(self):
        return self.disponivel and self.quantidade > 0

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('ativo', 'Ativo'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'),
    ]
    
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateField()
    data_devolvido = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.username}"
    
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['-data_emprestimo']

# Perfil extendido do usuário
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='perfis/', null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

# Signal para criar perfil automaticamente
@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, **kwargs):
    instance.perfil.save()