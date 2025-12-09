from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views
from core.views import custom_logout

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('registro/', views.registro, name='registro'),
    
    # Páginas principais
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('perfil/', views.perfil, name='perfil'),
    
    # CRUD Livros
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/<int:livro_id>/', views.detalhar_livro, name='detalhar_livro'),
    path('livros/adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('livros/<int:livro_id>/editar/', views.editar_livro, name='editar_livro'),
    path('livros/<int:livro_id>/excluir/', views.excluir_livro, name='excluir_livro'),
]

# Para servir arquivos de mídia em desenvolvimento
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)