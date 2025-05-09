# README - Sistema ERP em Django

Este projeto é um sistema ERP (Enterprise Resource Planning) básico desenvolvido em Django, com base na pesquisa sobre os melhores sistemas ERP do mercado. O sistema inclui módulos para gestão financeira, estoque, vendas e recursos humanos.

## Estrutura do Projeto

O projeto está organizado nos seguintes módulos:

1. **Financeiro**: Gerenciamento de contas a pagar, contas a receber e fluxo de caixa.
2. **Estoque**: Controle de produtos, movimentações e fornecedores.
3. **Vendas**: Gestão de clientes, pedidos e itens de pedido.
4. **Recursos Humanos (RH)**: Administração de funcionários, departamentos, cargos e benefícios.

## Requisitos

- Python 3.8+
- Django 4.2+
- Pillow (para manipulação de imagens)

## Instalação

1. Clone o repositório:
```
git clone <url-do-repositorio>
cd erp_django_project
```

2. Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```
pip install django pillow
```

4. Execute as migrações:
```
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superusuário:
```
python manage.py createsuperuser
```

6. Inicie o servidor:
```
python manage.py runserver
```

7. Acesse o sistema em: http://127.0.0.1:8000/

## Funcionalidades Implementadas

### Módulo Financeiro
- Gestão de contas a pagar e receber
- Controle de fluxo de caixa
- Dashboard financeiro

### Módulo de Estoque
- Cadastro e controle de produtos
- Registro de movimentações (entradas e saídas)
- Gestão de fornecedores

### Módulo de Vendas
- Cadastro de clientes
- Gestão de pedidos
- Controle de itens de pedido

### Módulo de RH
- Cadastro de funcionários
- Gestão de departamentos e cargos
- Controle de benefícios

### Sistema de Autenticação e Permissões
- Modelo de usuário personalizado
- Diferentes níveis de acesso (admin, financeiro, estoque, vendas, rh, visualizador)
- Controle de permissões por tipo de usuário

## Estrutura de Arquivos

```
erp_django_project/
├── erp_core/              # Aplicação principal
│   ├── models.py          # Modelo de usuário personalizado
│   ├── auth_views.py      # Views de autenticação
│   ├── settings.py        # Configurações do projeto
│   └── urls.py            # URLs do projeto
├── financeiro/            # Módulo financeiro
│   ├── models.py          # Modelos para contas a pagar, receber e fluxo de caixa
│   ├── views.py           # Views do módulo financeiro
│   └── urls.py            # URLs do módulo financeiro
├── estoque/               # Módulo de estoque
│   ├── models.py          # Modelos para produtos, movimentações e fornecedores
│   ├── views.py           # Views do módulo de estoque
│   └── urls.py            # URLs do módulo de estoque
├── vendas/                # Módulo de vendas
│   ├── models.py          # Modelos para clientes, pedidos e itens
│   ├── views.py           # Views do módulo de vendas
│   └── urls.py            # URLs do módulo de vendas
├── rh/                    # Módulo de recursos humanos
│   ├── models.py          # Modelos para funcionários, departamentos, cargos e benefícios
│   ├── views.py           # Views do módulo de RH
│   └── urls.py            # URLs do módulo de RH
├── templates/             # Templates HTML
│   ├── base.html          # Template base
│   ├── auth/              # Templates de autenticação
│   ├── financeiro/        # Templates do módulo financeiro
│   ├── estoque/           # Templates do módulo de estoque
│   ├── vendas/            # Templates do módulo de vendas
│   └── rh/                # Templates do módulo de RH
└── manage.py              # Script de gerenciamento do Django
```

## Próximos Passos

Este é um sistema ERP básico que pode ser expandido com as seguintes funcionalidades:

1. Implementação de relatórios detalhados
2. Integração com APIs de pagamento
3. Implementação de gráficos e dashboards mais avançados
4. Desenvolvimento de aplicativo móvel
5. Integração com sistemas de e-commerce

## Observações

- Este projeto foi desenvolvido como um exemplo básico e não deve ser usado em produção sem revisões de segurança adequadas.
- A senha padrão para novos usuários é "senha123" e deve ser alterada em um ambiente de produção.
- O sistema usa SQLite como banco de dados por padrão, mas pode ser configurado para usar PostgreSQL, MySQL ou outro banco de dados suportado pelo Django.
#   e r p _ d j a n g o _ p r o j e c t  
 