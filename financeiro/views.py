from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ContaAPagar, ContaAReceber, FluxoCaixa
from django.db.models import Sum
from django.utils import timezone

def index(request):
    # Resumo financeiro para o dashboard
    contas_a_pagar_pendentes = ContaAPagar.objects.filter(pago=False).count()
    contas_a_receber_pendentes = ContaAReceber.objects.filter(recebido=False).count()
    
    total_a_pagar = ContaAPagar.objects.filter(pago=False).aggregate(total=Sum('valor'))['total'] or 0
    total_a_receber = ContaAReceber.objects.filter(recebido=False).aggregate(total=Sum('valor'))['total'] or 0
    
    # Últimos registros de fluxo de caixa
    ultimos_fluxos = FluxoCaixa.objects.all().order_by('-data')[:5]
    
    context = {
        'contas_a_pagar_pendentes': contas_a_pagar_pendentes,
        'contas_a_receber_pendentes': contas_a_receber_pendentes,
        'total_a_pagar': total_a_pagar,
        'total_a_receber': total_a_receber,
        'ultimos_fluxos': ultimos_fluxos,
    }
    
    return render(request, 'financeiro/index.html', context)

# Views para Contas a Pagar
def contas_a_pagar_list(request):
    contas = ContaAPagar.objects.all().order_by('data_vencimento')
    return render(request, 'financeiro/contas_a_pagar_list.html', {'contas': contas})

def conta_a_pagar_detail(request, pk):
    conta = get_object_or_404(ContaAPagar, pk=pk)
    return render(request, 'financeiro/conta_a_pagar_detail.html', {'conta': conta})

def conta_a_pagar_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Conta a pagar criada com sucesso!')
        return redirect('financeiro:contas_a_pagar_list')
    return render(request, 'financeiro/conta_a_pagar_form.html')

def conta_a_pagar_update(request, pk):
    conta = get_object_or_404(ContaAPagar, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Conta a pagar atualizada com sucesso!')
        return redirect('financeiro:conta_a_pagar_detail', pk=conta.pk)
    return render(request, 'financeiro/conta_a_pagar_form.html', {'conta': conta})

def conta_a_pagar_delete(request, pk):
    conta = get_object_or_404(ContaAPagar, pk=pk)
    if request.method == 'POST':
        conta.delete()
        messages.success(request, 'Conta a pagar excluída com sucesso!')
        return redirect('financeiro:contas_a_pagar_list')
    return render(request, 'financeiro/conta_a_pagar_confirm_delete.html', {'conta': conta})

# Views para Contas a Receber
def contas_a_receber_list(request):
    contas = ContaAReceber.objects.all().order_by('data_vencimento')
    return render(request, 'financeiro/contas_a_receber_list.html', {'contas': contas})

def conta_a_receber_detail(request, pk):
    conta = get_object_or_404(ContaAReceber, pk=pk)
    return render(request, 'financeiro/conta_a_receber_detail.html', {'conta': conta})

def conta_a_receber_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Conta a receber criada com sucesso!')
        return redirect('financeiro:contas_a_receber_list')
    return render(request, 'financeiro/conta_a_receber_form.html')

def conta_a_receber_update(request, pk):
    conta = get_object_or_404(ContaAReceber, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Conta a receber atualizada com sucesso!')
        return redirect('financeiro:conta_a_receber_detail', pk=conta.pk)
    return render(request, 'financeiro/conta_a_receber_form.html', {'conta': conta})

def conta_a_receber_delete(request, pk):
    conta = get_object_or_404(ContaAReceber, pk=pk)
    if request.method == 'POST':
        conta.delete()
        messages.success(request, 'Conta a receber excluída com sucesso!')
        return redirect('financeiro:contas_a_receber_list')
    return render(request, 'financeiro/conta_a_receber_confirm_delete.html', {'conta': conta})

# Views para Fluxo de Caixa
def fluxo_caixa_list(request):
    fluxos = FluxoCaixa.objects.all().order_by('-data')
    return render(request, 'financeiro/fluxo_caixa_list.html', {'fluxos': fluxos})

def fluxo_caixa_detail(request, pk):
    fluxo = get_object_or_404(FluxoCaixa, pk=pk)
    return render(request, 'financeiro/fluxo_caixa_detail.html', {'fluxo': fluxo})

def fluxo_caixa_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Registro de fluxo de caixa criado com sucesso!')
        return redirect('financeiro:fluxo_caixa_list')
    return render(request, 'financeiro/fluxo_caixa_form.html')

def fluxo_caixa_update(request, pk):
    fluxo = get_object_or_404(FluxoCaixa, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Registro de fluxo de caixa atualizado com sucesso!')
        return redirect('financeiro:fluxo_caixa_detail', pk=fluxo.pk)
    return render(request, 'financeiro/fluxo_caixa_form.html', {'fluxo': fluxo})

def fluxo_caixa_delete(request, pk):
    fluxo = get_object_or_404(FluxoCaixa, pk=pk)
    if request.method == 'POST':
        fluxo.delete()
        messages.success(request, 'Registro de fluxo de caixa excluído com sucesso!')
        return redirect('financeiro:fluxo_caixa_list')
    return render(request, 'financeiro/fluxo_caixa_confirm_delete.html', {'fluxo': fluxo})
