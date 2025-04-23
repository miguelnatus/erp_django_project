from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redireciona para a página solicitada ou para o dashboard
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema com sucesso.')
    return redirect('login')

@login_required
def perfil_view(request):
    return render(request, 'auth/perfil.html')

@login_required
@permission_required('auth.add_user', raise_exception=True)
def usuario_list(request):
    from erp_core.models import Usuario
    usuarios = Usuario.objects.all().order_by('username')
    return render(request, 'auth/usuario_list.html', {'usuarios': usuarios})

class UsuarioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    from erp_core.models import Usuario
    model = Usuario
    template_name = 'auth/usuario_form.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'tipo', 'telefone', 'cargo', 'departamento']
    success_url = reverse_lazy('usuario_list')
    permission_required = 'auth.add_user'
    
    def form_valid(self, form):
        # Gera uma senha padrão para o novo usuário
        user = form.save(commit=False)
        password = 'senha123'  # Em produção, gerar senha aleatória e enviar por email
        user.set_password(password)
        messages.success(self.request, f'Usuário criado com sucesso. Senha inicial: {password}')
        return super().form_valid(form)

class UsuarioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    from erp_core.models import Usuario
    model = Usuario
    template_name = 'auth/usuario_form.html'
    fields = ['first_name', 'last_name', 'email', 'tipo', 'telefone', 'cargo', 'departamento', 'is_active']
    success_url = reverse_lazy('usuario_list')
    permission_required = 'auth.change_user'
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuário atualizado com sucesso.')
        return super().form_valid(form)
