from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, Pedido, ItemPedido
from estoque.models import Produto
from django.db.models import Sum, Count

def index(request):
    # Resumo de vendas para o dashboard
    total_pedidos = Pedido.objects.count()
    pedidos_pendentes = Pedido.objects.filter(status='pendente').count()
    total_clientes = Cliente.objects.count()
    
    # Valor total de vendas
    valor_total_vendas = Pedido.objects.filter(status__in=['aprovado', 'em_separacao', 'enviado', 'entregue']).aggregate(
        total=Sum('valor_final'))['total'] or 0
    
    # Últimos pedidos
    ultimos_pedidos = Pedido.objects.all().order_by('-data_pedido')[:5]
    
    context = {
        'total_pedidos': total_pedidos,
        'pedidos_pendentes': pedidos_pendentes,
        'total_clientes': total_clientes,
        'valor_total_vendas': valor_total_vendas,
        'ultimos_pedidos': ultimos_pedidos,
    }
    
    return render(request, 'vendas/index.html', context)

# Views para Clientes
def cliente_list(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'vendas/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    pedidos = cliente.pedidos.all().order_by('-data_pedido')
    return render(request, 'vendas/cliente_detail.html', {
        'cliente': cliente,
        'pedidos': pedidos
    })

def cliente_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Cliente criado com sucesso!')
        return redirect('vendas:cliente_list')
    return render(request, 'vendas/cliente_form.html')

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Cliente atualizado com sucesso!')
        return redirect('vendas:cliente_detail', pk=cliente.pk)
    return render(request, 'vendas/cliente_form.html', {'cliente': cliente})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return redirect('vendas:cliente_list')
    return render(request, 'vendas/cliente_confirm_delete.html', {'cliente': cliente})

# Views para Pedidos
def pedido_list(request):
    pedidos = Pedido.objects.all().order_by('-data_pedido')
    return render(request, 'vendas/pedido_list.html', {'pedidos': pedidos})

def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    itens = pedido.itens.all()
    return render(request, 'vendas/pedido_detail.html', {
        'pedido': pedido,
        'itens': itens
    })

def pedido_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Pedido criado com sucesso!')
        return redirect('vendas:pedido_list')
    
    # Obter lista de clientes para o formulário
    clientes = Cliente.objects.filter(ativo=True).order_by('nome')
    return render(request, 'vendas/pedido_form.html', {'clientes': clientes})

def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Pedido atualizado com sucesso!')
        return redirect('vendas:pedido_detail', pk=pedido.pk)
    return render(request, 'vendas/pedido_form.html', {'pedido': pedido})

def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido excluído com sucesso!')
        return redirect('vendas:pedido_list')
    return render(request, 'vendas/pedido_confirm_delete.html', {'pedido': pedido})

# Views para Itens de Pedido
def item_pedido_create(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Item adicionado ao pedido com sucesso!')
        return redirect('vendas:pedido_detail', pk=pedido.pk)
    
    # Obter lista de produtos para o formulário
    produtos = Produto.objects.filter(ativo=True).order_by('nome')
    return render(request, 'vendas/item_pedido_form.html', {
        'pedido': pedido,
        'produtos': produtos
    })

def item_pedido_delete(request, pk):
    item = get_object_or_404(ItemPedido, pk=pk)
    pedido_id = item.pedido.id
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item removido do pedido com sucesso!')
        return redirect('vendas:pedido_detail', pk=pedido_id)
    return render(request, 'vendas/item_pedido_confirm_delete.html', {'item': item})
