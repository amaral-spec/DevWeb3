📚 Sistema de Biblioteca com Django
👥 Membros do Grupo
Gabriel Amaral - CP3025624
Emilly Cabuçu - CP3025781

🎯 Descrição do Projeto
Sistema web completo para gestão de bibliotecas desenvolvido com Django Framework. O sistema permite o gerenciamento de livros, autores, categorias e empréstimos, implementando operações CRUD completas com interface moderna e responsiva.

🛠 Tecnologias Utilizadas
Backend
Python 3.10+

Django 4.2.7

SQLite (desenvolvimento)

Django Crispy Forms

Pillow (manipulação de imagens)

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
text
biblioteca_django/
├── biblioteca/                 # Configuração do projeto Django
│   ├── __init__.py
│   ├── settings.py            # Configurações
│   ├── urls.py                # Rotas principais
│   └── wsgi.py
├── core/                      # Aplicação principal
│   ├── migrations/           # Migrações do banco
│   ├── models.py            # Modelos de dados
│   ├── views.py             # Lógica da aplicação
│   ├── admin.py             # Painel administrativo
│   └── templates/core/      # Templates HTML
├── static/                   # Arquivos estáticos
├── media/                    # Uploads de arquivos
├── templates/               # Templates base
│   ├── base.html
│   └── registration/
├── db.sqlite3               # Banco de dados
├── manage.py                # Script de gerenciamento
├── requirements.txt         # Dependências Python
└── README.md               # Esta documentação
🗃️ Modelos do Banco de Dados
1. Autor
nome (CharField): Nome completo do autor

nacionalidade (CharField): Nacionalidade

data_nascimento (DateField): Data de nascimento

biografia (TextField): Biografia do autor

2. Categoria
nome (CharField): Nome da categoria

descricao (TextField): Descrição detalhada

3. Livro ✅ CRUD COMPLETO
titulo (CharField): Título do livro

autor (ForeignKey): Relacionamento com Autor

isbn (CharField): ISBN único (13 dígitos)

editora (CharField): Editora

ano_publicacao (IntegerField): Ano de publicação

categoria (ForeignKey): Relacionamento com Categoria

quantidade (IntegerField): Quantidade disponível

disponivel (BooleanField): Status de disponibilidade

sinopse (TextField): Sinopse do livro

capa (ImageField): Imagem da capa (opcional)

data_cadastro (DateTimeField): Data de cadastro automática

4. Empréstimo ✅ CRUD COMPLETO
livro (ForeignKey): Livro emprestado

usuario (ForeignKey): Usuário que fez o empréstimo

data_emprestimo (DateTimeField): Data do empréstimo

data_devolucao (DateField): Data prevista para devolução

data_devolvido (DateField): Data real da devolução

status (CharField): Status (pendente/ativo/devolvido/atrasado)

observacoes (TextField): Observações

5. Perfil ✅ CRUD COMPLETO
user (OneToOneField): Relacionamento com User do Django

telefone (CharField): Telefone do usuário

endereco (TextField): Endereço completo

cpf (CharField): CPF (único)

data_nascimento (DateField): Data de nascimento

foto (ImageField): Foto de perfil (opcional)

🌐 Endpoints da API
Rotas Principais
text
/                           → Página inicial
/login/                     → Login de usuários
/logout/                    → Logout seguro
/registro/                  → Registro de novos usuários
/sobre/                     → Página sobre o sistema
/perfil/                    → Perfil do usuário
CRUD Livros 📖
text
/livros/                    → Lista todos os livros (READ)
/livros/adicionar/          → Adicionar novo livro (CREATE)
/livros/<id>/               → Detalhes do livro (READ)
/livros/<id>/editar/        → Editar livro existente (UPDATE)
/livros/<id>/excluir/       → Excluir livro (DELETE)
Painel Administrativo
text
/admin/                     → Painel administrativo Django
💻 Funcionalidades Implementadas
✅ Autenticação e Autorização
Sistema completo de login/logout

Registro de novos usuários

Páginas protegidas por autenticação

Perfil de usuário personalizado

✅ CRUD Completo (3 CRUDs)
Livros - Create, Read, Update, Delete

Autores - Create, Read, Update, Delete

Empréstimos - Create, Read, Update, Delete

✅ Interface do Usuário
Design responsivo com Bootstrap 5

Navegação intuitiva

Formulários validados

Mensagens de feedback

Upload de imagens (capas e fotos)

✅ Painel Administrativo
Interface Django Admin customizada

Filtros e buscas avançadas

Gerenciamento completo de dados

Exportação de dados

🚀 Instalação e Configuração
Pré-requisitos
Python 3.10 ou superior

Pip (gerenciador de pacotes Python)

Git (opcional)

Passo 1: Clonar o repositório
bash
git clone https://github.com/seu-usuario/biblioteca-django.git
cd biblioteca-django
Passo 2: Criar ambiente virtual
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Passo 3: Instalar dependências
bash
pip install -r requirements.txt
Passo 4: Configurar banco de dados
bash
python manage.py makemigrations
python manage.py migrate
Passo 5: Criar superusuário
bash
python manage.py createsuperuser
# Siga as instruções para criar usuário admin
Passo 6: Coletar arquivos estáticos
bash
python manage.py collectstatic
Passo 7: Executar servidor de desenvolvimento
bash
python manage.py runserver
Passo 8: Acessar a aplicação
text
Navegador: http://localhost:8000
Admin:     http://localhost:8000/admin
📊 Populando o Banco de Dados
Opção 1: Via Painel Admin
Acesse http://localhost:8000/admin

Use as credenciais do superusuário

Adicione dados manualmente

Opção 2: Via Shell Django
bash
python manage.py shell
python
from core.models import Autor, Categoria, Livro

# Criar categorias
categorias = ['Ficção', 'Tecnologia', 'História', 'Ciência', 'Literatura']
for nome in categorias:
    Categoria.objects.get_or_create(nome=nome)

# Criar autores
autores = [
    {'nome': 'Machado de Assis', 'nacionalidade': 'Brasileiro'},
    {'nome': 'George Orwell', 'nacionalidade': 'Britânico'},
    {'nome': 'Stephen King', 'nacionalidade': 'Americano'},
]

for autor_data in autores:
    Autor.objects.get_or_create(**autor_data)

# Criar livros de exemplo
livro1 = Livro.objects.create(
    titulo='Dom Casmurro',
    autor=Autor.objects.get(nome='Machado de Assis'),
    isbn='9788535930123',
    editora='Companhia das Letras',
    ano_publicacao=1899,
    categoria=Categoria.objects.get(nome='Literatura'),
    quantidade=5,
    disponivel=True,
    sinopse='Romance clássico da literatura brasileira'
)
🔧 Configurações Importantes
settings.py
python
# Configurações principais
DEBUG = True  # Alterar para False em produção
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# Arquivos estáticos e mídia
STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Autenticação
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
🧪 Testando o Sistema
Testes Manuais
Registro de Usuário

Acesse /registro/

Crie uma nova conta

Verifique login automático

CRUD Livros

Faça login

Acesse /livros/

Teste todas as operações:

Adicionar livro

Visualizar detalhes

Editar informações

Excluir registro

Painel Admin

Acesse /admin/

Gerencie todos os modelos

Teste filtros e buscas

📱 Telas do Sistema
1. Página Inicial
Apresentação do sistema

Estatísticas gerais

Livros recentes

Links rápidos

2. Listagem de Livros
Tabela com todos os livros

Filtros por status

Ações CRUD por linha

Paginação (se implementada)

3. Formulários
Validação em tempo real

Upload de imagens

Seleção por dropdown

Mensagens de erro/sucesso

4. Perfil do Usuário
Informações da conta

Foto de perfil

Histórico de empréstimos

Opções de configuração

🐛 Solução de Problemas
Problema 1: "ModuleNotFoundError"
bash
# Solução: Reinstalar dependências
pip install --upgrade pip
pip install -r requirements.txt
Problema 2: Erro de migração
bash
# Solução: Recriar migrações
python manage.py makemigrations
python manage.py migrate
Problema 3: Arquivos estáticos não carregam
bash
# Solução: Coletar arquivos estáticos
python manage.py collectstatic
Problema 4: Acesso negado ao admin
bash
# Solução: Criar/redefinir superusuário
python manage.py createsuperuser
