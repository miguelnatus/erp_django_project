from django.db import models
from django.utils import timezone

class Fornecedor(models.Model):
    nome        = models.CharField(max_length=200)
    cnpj        = models.CharField(max_length=18, unique=True)
    email       = models.EmailField()
    telefone    = models.CharField(max_length=15)
    endereco    = models.CharField(max_length=255)
    contato     = models.CharField(max_length=100, blank=True)
    cidade      = models.CharField(max_length=100, default='')
    estado      = models.CharField(max_length=2)
    cep         = models.CharField(max_length=9, blank=True, default='')
    observacoes = models.TextField(blank=True)
    ativo       = models.BooleanField(default=True)
    produtos    = models.ManyToManyField('Produto', related_name='fornecedores', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['nome']


class Produto(models.Model):
    UNIDADE_CHOICES = [
        ('un', 'Unidade'),
        ('kg', 'Quilograma'),
        ('l', 'Litro'),
        ('cx', 'Caixa'),
        ('pct', 'Pacote'),
    ]

    nome            = models.CharField(max_length=200)
    descricao       = models.TextField(blank=True)
    codigo          = models.CharField(max_length=50, unique=True)
    preco_custo     = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda     = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_medida  = models.CharField(max_length=3, choices=UNIDADE_CHOICES, default='un')
    estoque_atual   = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_minimo  = models.DecimalField(max_digits=10, decimal_places=2)
    categoria       = models.CharField(max_length=100)
    data_cadastro   = models.DateTimeField(default=timezone.now)
    ativo           = models.BooleanField(default=True)

    # novos campos
    localizacao     = models.CharField(max_length=100, blank=True)
    fornecedor      = models.ForeignKey(
        Fornecedor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='produtos_fornecidos'
    )

    def __str__(self):
        return f"{self.nome} ({self.codigo}) - Estoque: {self.estoque_atual} {self.unidade_medida}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']

    @property
    def estoque_baixo(self):
        return self.estoque_atual <= self.estoque_minimo


class Movimentacao(models.Model):
    TIPO_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida',   'Saída'),
    ]

    produto        = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='movimentacoes')
    tipo           = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade     = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data           = models.DateTimeField(default=timezone.now)
    responsavel    = models.CharField(max_length=200)
    observacao     = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} de {self.quantidade} {self.produto.unidade_medida} de {self.produto.nome}"

    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        ordering = ['-data']

    def save(self, *args, **kwargs):
        if self.tipo == 'entrada':
            self.produto.estoque_atual += self.quantidade
        else:
            self.produto.estoque_atual -= self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)
