from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    """
    Modelo de usuário personalizado para o sistema ERP.
    Estende o modelo de usuário padrão do Django para adicionar campos específicos.
    """
    TIPO_CHOICES = [
        ('admin', 'Administrador'),
        ('financeiro', 'Financeiro'),
        ('estoque', 'Estoque'),
        ('vendas', 'Vendas'),
        ('rh', 'Recursos Humanos'),
        ('visualizador', 'Visualizador'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='visualizador')
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    data_ultimo_acesso = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = [
            ('acesso_financeiro', 'Pode acessar o módulo financeiro'),
            ('acesso_estoque', 'Pode acessar o módulo de estoque'),
            ('acesso_vendas', 'Pode acessar o módulo de vendas'),
            ('acesso_rh', 'Pode acessar o módulo de RH'),
            ('gerar_relatorios', 'Pode gerar relatórios'),
        ]
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # Ao criar um novo usuário, atribui permissões com base no tipo
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            self.atribuir_permissoes_por_tipo()
    
    def atribuir_permissoes_por_tipo(self):
        """Atribui permissões com base no tipo de usuário"""
        # Limpa permissões existentes
        self.user_permissions.clear()
        
        # Atribui permissões com base no tipo
        if self.tipo == 'admin':
            # Administrador tem todas as permissões
            for perm in Permission.objects.all():
                self.user_permissions.add(perm)
        
        elif self.tipo == 'financeiro':
            # Permissões para usuários do financeiro
            self.user_permissions.add(Permission.objects.get(codename='acesso_financeiro'))
            self.user_permissions.add(Permission.objects.get(codename='gerar_relatorios'))
        
        elif self.tipo == 'estoque':
            # Permissões para usuários do estoque
            self.user_permissions.add(Permission.objects.get(codename='acesso_estoque'))
            self.user_permissions.add(Permission.objects.get(codename='gerar_relatorios'))
        
        elif self.tipo == 'vendas':
            # Permissões para usuários de vendas
            self.user_permissions.add(Permission.objects.get(codename='acesso_vendas'))
            self.user_permissions.add(Permission.objects.get(codename='gerar_relatorios'))
        
        elif self.tipo == 'rh':
            # Permissões para usuários de RH
            self.user_permissions.add(Permission.objects.get(codename='acesso_rh'))
            self.user_permissions.add(Permission.objects.get(codename='gerar_relatorios'))
        
        # Visualizador não recebe permissões específicas
