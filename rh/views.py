from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Departamento, Cargo, Funcionario, Beneficio, BeneficioFuncionario
from django.db.models import Sum, Count
from django.utils import timezone

def index(request):
    # Resumo de RH para o dashboard
    total_funcionarios = Funcionario.objects.filter(ativo=True).count()
    total_departamentos = Departamento.objects.count()
    total_cargos = Cargo.objects.count()
    
    # Funcionários por departamento
    funcionarios_por_departamento = Departamento.objects.annotate(
        total_funcionarios=Count('funcionarios')).order_by('-total_funcionarios')
    
    # Últimos funcionários cadastrados
    ultimos_funcionarios = Funcionario.objects.filter(ativo=True).order_by('-data_admissao')[:5]
    
    context = {
        'total_funcionarios': total_funcionarios,
        'total_departamentos': total_departamentos,
        'total_cargos': total_cargos,
        'funcionarios_por_departamento': funcionarios_por_departamento,
        'ultimos_funcionarios': ultimos_funcionarios,
    }
    
    return render(request, 'rh/index.html', context)

# Views para Departamentos
def departamento_list(request):
    departamentos = Departamento.objects.all().order_by('nome')
    return render(request, 'rh/departamento_list.html', {'departamentos': departamentos})

def departamento_detail(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    funcionarios = departamento.funcionarios.filter(ativo=True)
    cargos = departamento.cargos.all()
    return render(request, 'rh/departamento_detail.html', {
        'departamento': departamento,
        'funcionarios': funcionarios,
        'cargos': cargos
    })

def departamento_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Departamento criado com sucesso!')
        return redirect('rh:departamento_list')
    return render(request, 'rh/departamento_form.html')

def departamento_update(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Departamento atualizado com sucesso!')
        return redirect('rh:departamento_detail', pk=departamento.pk)
    return render(request, 'rh/departamento_form.html', {'departamento': departamento})

def departamento_delete(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == 'POST':
        departamento.delete()
        messages.success(request, 'Departamento excluído com sucesso!')
        return redirect('rh:departamento_list')
    return render(request, 'rh/departamento_confirm_delete.html', {'departamento': departamento})

# Views para Cargos
def cargo_list(request):
    cargos = Cargo.objects.all().order_by('departamento', 'nome')
    return render(request, 'rh/cargo_list.html', {'cargos': cargos})

def cargo_detail(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    funcionarios = cargo.funcionarios.filter(ativo=True)
    return render(request, 'rh/cargo_detail.html', {
        'cargo': cargo,
        'funcionarios': funcionarios
    })

def cargo_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Cargo criado com sucesso!')
        return redirect('rh:cargo_list')
    
    # Obter lista de departamentos para o formulário
    departamentos = Departamento.objects.all().order_by('nome')
    return render(request, 'rh/cargo_form.html', {'departamentos': departamentos})

def cargo_update(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Cargo atualizado com sucesso!')
        return redirect('rh:cargo_detail', pk=cargo.pk)
    
    # Obter lista de departamentos para o formulário
    departamentos = Departamento.objects.all().order_by('nome')
    return render(request, 'rh/cargo_form.html', {
        'cargo': cargo,
        'departamentos': departamentos
    })

def cargo_delete(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        messages.success(request, 'Cargo excluído com sucesso!')
        return redirect('rh:cargo_list')
    return render(request, 'rh/cargo_confirm_delete.html', {'cargo': cargo})

# Views para Funcionários
def funcionario_list(request):
    funcionarios = Funcionario.objects.filter(ativo=True).order_by('nome')
    return render(request, 'rh/funcionario_list.html', {'funcionarios': funcionarios})

def funcionario_detail(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    beneficios = funcionario.beneficios.all()
    return render(request, 'rh/funcionario_detail.html', {
        'funcionario': funcionario,
        'beneficios': beneficios
    })

def funcionario_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Funcionário cadastrado com sucesso!')
        return redirect('rh:funcionario_list')
    
    # Obter listas para o formulário
    departamentos = Departamento.objects.all().order_by('nome')
    cargos = Cargo.objects.all().order_by('nome')
    return render(request, 'rh/funcionario_form.html', {
        'departamentos': departamentos,
        'cargos': cargos
    })

def funcionario_update(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Funcionário atualizado com sucesso!')
        return redirect('rh:funcionario_detail', pk=funcionario.pk)
    
    # Obter listas para o formulário
    departamentos = Departamento.objects.all().order_by('nome')
    cargos = Cargo.objects.all().order_by('nome')
    return render(request, 'rh/funcionario_form.html', {
        'funcionario': funcionario,
        'departamentos': departamentos,
        'cargos': cargos
    })

def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        # Em vez de excluir, apenas marcamos como inativo
        funcionario.ativo = False
        funcionario.data_demissao = timezone.now().date()
        funcionario.save()
        messages.success(request, 'Funcionário desligado com sucesso!')
        return redirect('rh:funcionario_list')
    return render(request, 'rh/funcionario_confirm_delete.html', {'funcionario': funcionario})

# Views para Benefícios
def beneficio_list(request):
    beneficios = Beneficio.objects.all().order_by('nome')
    return render(request, 'rh/beneficio_list.html', {'beneficios': beneficios})

def beneficio_detail(request, pk):
    beneficio = get_object_or_404(Beneficio, pk=pk)
    funcionarios = Funcionario.objects.filter(beneficios__beneficio=beneficio, ativo=True)
    return render(request, 'rh/beneficio_detail.html', {
        'beneficio': beneficio,
        'funcionarios': funcionarios
    })

def beneficio_create(request):
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Benefício criado com sucesso!')
        return redirect('rh:beneficio_list')
    return render(request, 'rh/beneficio_form.html')

def beneficio_update(request, pk):
    beneficio = get_object_or_404(Beneficio, pk=pk)
    if request.method == 'POST':
        # Aqui seria implementado o processamento do formulário
        # Por simplicidade, estamos apenas simulando
        messages.success(request, 'Benefício atualizado com sucesso!')
        return redirect('rh:beneficio_detail', pk=beneficio.pk)
    return render(request, 'rh/beneficio_form.html', {'beneficio': beneficio})

def beneficio_delete(request, pk):
    beneficio = get_object_or_404(Beneficio, pk=pk)
    if request.method == 'POST':
        beneficio.delete()
        messages.success(request, 'Benefício excluído com sucesso!')
        return redirect('rh:beneficio_list')
    return render(request, 'rh/beneficio_confirm_delete.html', {'beneficio': beneficio})
