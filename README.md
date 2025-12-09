📚 Sistema de Biblioteca com Django
👥 Membros do Grupo

Gabriel Amaral – CP3025624

Emilly Cabuçu – CP3025781

🎯 Descrição do Projeto

Sistema web completo para gestão de bibliotecas desenvolvido com Django Framework.
O sistema permite o gerenciamento de livros, autores, categorias e empréstimos, implementando operações CRUD completas, com interface moderna e responsiva baseada em Bootstrap.

🛠 Tecnologias Utilizadas
Backend

Python 3.10+

Django 4.2.7

SQLite (Ambiente de desenvolvimento)

Django Crispy Forms

Pillow (upload de imagens)

Frontend

HTML5

CSS3

Bootstrap 5.3.0

JavaScript

Bootstrap Icons

Ferramentas de Desenvolvimento

Git

Visual Studio Code

DB Browser for SQLite

Postman (testes de API)

📁 Estrutura do Projeto
biblioteca_django/
├── biblioteca/                 # Configuração do projeto Django
│   ├── __init__.py
│   ├── settings.py             # Configurações gerais
│   ├── urls.py                 # Rotas principais
│   └── wsgi.py
├── core/                       # Aplicação principal
│   ├── migrations/             # Migrações do banco
│   ├── models.py               # Modelos de dados
│   ├── views.py                # Regras de negócio
│   ├── admin.py                # Admin Django
│   └── templates/core/         # Templates HTML da aplicação
├── static/                     # Arquivos estáticos
├── media/                      # Uploads (capas, fotos)
├── templates/                  # Templates globais
│   ├── base.html
│   └── registration/           # Telas de login/registro
├── db.sqlite3                  # Banco de dados
├── manage.py                   # Script de gerenciamento Django
├── requirements.txt            # Dependências Python
└── README.md

🗃️ Modelos do Banco de Dados
1. Autor

nome

nacionalidade

data_nascimento

biografia

2. Categoria

nome

descricao

3. Livro (CRUD COMPLETO)

titulo

autor (ForeignKey)

isbn

editora

ano_publicacao

categoria (ForeignKey)

quantidade

disponivel

sinopse

capa (ImageField)

data_cadastro

4. Empréstimo (CRUD COMPLETO)

livro (ForeignKey)

usuario (ForeignKey)

data_emprestimo

data_devolucao

data_devolvido

status

observacoes

5. Perfil (CRUD COMPLETO)

user (OneToOne)

telefone

endereco

cpf

data_nascimento

foto

🌐 Endpoints / Rotas Principais
Autenticação
/login/                
/logout/               
/registro/

Páginas Gerais
/                      → Página inicial
/sobre/                → Sobre o sistema
/perfil/               → Perfil do usuário

Livros – CRUD
/livros/               → Listagem
/livros/adicionar/     → Criar
/livros/<id>/          → Detalhes
/livros/<id>/editar/   → Atualizar
/livros/<id>/excluir/  → Deletar

Admin Django
/admin/

💻 Funcionalidades Implementadas
✅ Autenticação Completa

Login / Logout

Registro de usuários

Perfil personalizado

Acesso restrito por login

✅ CRUDs Completos (3 obrigatórios)

Livros

Autores

Empréstimos

✅ Interface Moderna

Bootstrap 5

Layout responsivo

Formulários validados

Upload de imagens

✅ Painel Administrativo

Filtros, busca e ordenação

Edição rápida

Gerenciamento completo dos dados

🚀 Instalação e Configuração
Pré-requisitos

Python 3.10+

Pip

Git

1. Clonar o Repositório
git clone https://github.com/amaral-spec/DevWeb3.git
cd biblioteca-django

2. Criar Ambiente Virtual
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Instalar Dependências
pip install -r requirements.txt

4. Fazer Migrações
python manage.py makemigrations
python manage.py migrate

5. Criar Superusuário
python manage.py createsuperuser

6. Coletar Arquivos Estáticos
python manage.py collectstatic

7. Executar o Servidor
python manage.py runserver

8. Acessar o Sistema
Aplicação: http://localhost:8000
Admin:     http://localhost:8000/admin

📊 Populando o Banco de Dados
Via Django Admin

Acesse /admin

Use o superusuário criado

Adicione autores, livros e categorias

Via Shell Django
from core.models import Autor, Categoria, Livro

Categoria.objects.create(nome='Tecnologia')
Autor.objects.create(nome='George Orwell', nacionalidade='Britânico')

Livro.objects.create(
    titulo='1984',
    autor=Autor.objects.get(nome='George Orwell'),
    isbn='9780451524935',
    editora='Secker & Warburg',
    ano_publicacao=1949,
    categoria=Categoria.objects.get(nome='Tecnologia'),
    quantidade=10,
    disponivel=True,
    sinopse='Clássico distópico.'
)

🔧 Configurações Importantes
settings.py
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

🧪 Testes do Sistema
Testes Manuais

Registro

Login

CRUD de livros

CRUD de autores

CRUD de empréstimos

Painel administrativo

📱 Telas do Sistema

Página inicial dinâmica

Listagem de livros

Formulários com validação

Perfil de usuário

Painel admin

🐛 Solução de Problemas
1. ModuleNotFoundError
pip install -r requirements.txt

2. Erros de migração
python manage.py makemigrations
python manage.py migrate

3. Arquivos estáticos não carregam
python manage.py collectstatic

4. Não consegue acessar o admin
python manage.py createsuperuser

📄 Licença

Este projeto foi desenvolvido para fins educacionais.

Se quiser, posso agora:

✅ Criar o arquivo README.md automaticamente
✅ Gerar todo o projeto Django
✅ Criar todos os modelos, views, templates e URLs
✅ Criar CRUD completo
✅ Criar interface Bootstrap pronta
