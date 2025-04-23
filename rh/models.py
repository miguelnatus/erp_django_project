from django.db import models
from django.utils import timezone

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    responsavel = models.ForeignKey('Funcionario', on_delete=models.SET_NULL, null=True, blank=True, related_name='departamentos_chefiados')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['nome']

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='cargos')
    
    def __str__(self):
        return f"{self.nome} - {self.departamento.nome}"
    
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['departamento', 'nome']

class Funcionario(models.Model):
    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'),
    ]
    
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    data_admissao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='funcionarios')
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='funcionarios')
    salario_atual = models.DecimalField(max_digits=10, decimal_places=2)
    estado_civil = models.CharField(max_length=15, choices=ESTADO_CIVIL_CHOICES)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nome} - {self.cargo.nome}"
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ['nome']
    
    @property
    def tempo_empresa(self):
        if self.data_demissao:
            return (self.data_demissao - self.data_admissao).days
        return (timezone.now().date() - self.data_admissao).days

class Beneficio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Benefício"
        verbose_name_plural = "Benefícios"

class BeneficioFuncionario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='beneficios')
    beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    valor_personalizado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.beneficio.nome} - {self.funcionario.nome}"
    
    class Meta:
        verbose_name = "Benefício do Funcionário"
        verbose_name_plural = "Benefícios dos Funcionários"
        unique_together = ['funcionario', 'beneficio']
