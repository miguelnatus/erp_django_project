from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib import messages
from .models import Produto, Fornecedor, Movimentacao
from .forms import ProdutoForm, FornecedorForm, MovimentacaoForm

def index(request):
    """
    View para a página inicial do módulo de estoque.
    """
    total_produtos = Produto.objects.count()
    total_fornecedores = Fornecedor.objects.count()
    total_movimentacoes = Movimentacao.objects.count()
    produtos_estoque_baixo = Produto.objects.filter(estoque_atual__lte=models.F('estoque_minimo')).count()
    
    # Obter produtos com estoque baixo para exibir na tabela
    produtos_estoque_baixo_lista = Produto.objects.filter(
        estoque_atual__lte=models.F('estoque_minimo')
    ).order_by('estoque_atual')[:5]
    
    # Obter últimas movimentações para exibir na tabela
    ultimas_movimentacoes = Movimentacao.objects.all().order_by('-data')[:5]
    
    context = {
        'total_produtos': total_produtos,
        'total_fornecedores': total_fornecedores,
        'total_movimentacoes': total_movimentacoes,
        'produtos_estoque_baixo': produtos_estoque_baixo,
        'produtos_estoque_baixo_lista': produtos_estoque_baixo_lista,
        'ultimas_movimentacoes': ultimas_movimentacoes,
    }
    
    return render(request, 'estoque/dashboard.html', context)

def produto_list(request):
    """
    View para listar todos os produtos.
    """
    produtos = Produto.objects.all()
    return render(request, 'estoque/produto_list.html', {'produtos': produtos})

def produto_create(request):
    """
    View para criar um novo produto.
    """
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            messages.success(request, f'Produto "{produto.nome}" criado com sucesso!')
            return redirect('estoque:produto_list')
    else:
        form = ProdutoForm()
    
    return render(request, 'estoque/produto_form.html', {
        'form': form,
        'titulo': 'Novo Produto',
        'modo': 'criar'
    })

def produto_detail(request, pk):
    """
    View para exibir detalhes de um produto específico.
    """
    produto = get_object_or_404(Produto, pk=pk)
    movimentacoes = Movimentacao.objects.filter(produto=produto).order_by('-data')[:10]
    
    return render(request, 'estoque/produto_detail.html', {
        'produto': produto,
        'movimentacoes': movimentacoes
    })

def produto_update(request, pk):
    """
    View para atualizar um produto existente.
    """
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save()
            messages.success(request, f'Produto "{produto.nome}" atualizado com sucesso!')
            return redirect('estoque:produto_detail', pk=produto.pk)
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'estoque/produto_form.html', {
        'form': form,
        'produto': produto,
        'titulo': 'Editar Produto',
        'modo': 'editar'
    })

def produto_delete(request, pk):
    """
    View para excluir um produto existente.
    """
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        nome_produto = produto.nome
        produto.delete()
        messages.success(request, f'Produto "{nome_produto}" excluído com sucesso!')
        return redirect('estoque:produto_list')
    
    return render(request, 'estoque/produto_confirm_delete.html', {
        'produto': produto
    })

def fornecedor_list(request):
    """
    View para listar todos os fornecedores.
    """
    fornecedores = Fornecedor.objects.all()
    return render(request, 'estoque/fornecedor_list.html', {'fornecedores': fornecedores})

def fornecedor_create(request):
    """
    View para criar um novo fornecedor.
    """
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save()
            messages.success(request, f'Fornecedor "{fornecedor.nome}" criado com sucesso!')
            return redirect('estoque:fornecedor_list')
    else:
        form = FornecedorForm()
    
    return render(request, 'estoque/fornecedor_form.html', {
        'form': form,
        'titulo': 'Novo Fornecedor',
        'modo': 'criar'
    })

def fornecedor_detail(request, pk):
    """
    View para exibir detalhes de um fornecedor específico.
    """
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    produtos = Produto.objects.filter(fornecedor=fornecedor)
    
    return render(request, 'estoque/fornecedor_detail.html', {
        'fornecedor': fornecedor,
        'produtos': produtos
    })

def fornecedor_update(request, pk):
    """
    View para atualizar um fornecedor existente.
    """
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            fornecedor = form.save()
            messages.success(request, f'Fornecedor "{fornecedor.nome}" atualizado com sucesso!')
            return redirect('estoque:fornecedor_detail', pk=fornecedor.pk)
    else:
        form = FornecedorForm(instance=fornecedor)
    
    return render(request, 'estoque/fornecedor_form.html', {
        'form': form,
        'fornecedor': fornecedor,
        'titulo': 'Editar Fornecedor',
        'modo': 'editar'
    })

def fornecedor_delete(request, pk):
    """
    View para excluir um fornecedor existente.
    """
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    
    if request.method == 'POST':
        nome_fornecedor = fornecedor.nome
        fornecedor.delete()
        messages.success(request, f'Fornecedor "{nome_fornecedor}" excluído com sucesso!')
        return redirect('estoque:fornecedor_list')
    
    return render(request, 'estoque/fornecedor_confirm_delete.html', {
        'fornecedor': fornecedor
    })

def movimentacao_list(request):
    """
    View para listar todas as movimentações de estoque.
    """
    movimentacoes = Movimentacao.objects.all().order_by('-data')
    return render(request, 'estoque/movimentacao_list.html', {'movimentacoes': movimentacoes})

def movimentacao_create(request):
    """
    View para criar uma nova movimentação de estoque.
    """
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            
            # Atualizar o estoque do produto
            produto = movimentacao.produto
            if movimentacao.tipo == 'entrada':
                produto.estoque_atual += movimentacao.quantidade
            elif movimentacao.tipo == 'saida':
                if produto.estoque_atual >= movimentacao.quantidade:
                    produto.estoque_atual -= movimentacao.quantidade
                else:
                    messages.error(request, f'Estoque insuficiente para o produto "{produto.nome}"!')
                    return render(request, 'estoque/movimentacao_form.html', {
                        'form': form,
                        'titulo': 'Nova Movimentação',
                        'modo': 'criar'
                    })
            elif movimentacao.tipo == 'ajuste':
                produto.estoque_atual = movimentacao.quantidade
            
            produto.save()
            movimentacao.save()
            
            messages.success(request, 'Movimentação de estoque registrada com sucesso!')
            return redirect('estoque:movimentacao_list')
    else:
        form = MovimentacaoForm()
    
    return render(request, 'estoque/movimentacao_form.html', {
        'form': form,
        'titulo': 'Nova Movimentação',
        'modo': 'criar'
    })

def movimentacao_detail(request, pk):
    """
    View para exibir detalhes de uma movimentação específica.
    """
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    
    return render(request, 'estoque/movimentacao_detail.html', {
        'movimentacao': movimentacao
    })
