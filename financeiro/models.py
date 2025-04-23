from django.db import models
from django.utils import timezone

class ContaAPagar(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    pago = models.BooleanField(default=False)
    fornecedor = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.descricao} - R${self.valor} - {self.data_vencimento}"
    
    class Meta:
        verbose_name = "Conta a Pagar"
        verbose_name_plural = "Contas a Pagar"

class ContaAReceber(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    data_recebimento = models.DateField(null=True, blank=True)
    recebido = models.BooleanField(default=False)
    cliente = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.descricao} - R${self.valor} - {self.data_vencimento}"
    
    class Meta:
        verbose_name = "Conta a Receber"
        verbose_name_plural = "Contas a Receber"

class FluxoCaixa(models.Model):
    data = models.DateField()
    saldo_inicial = models.DecimalField(max_digits=12, decimal_places=2)
    entradas = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    saidas = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    saldo_final = models.DecimalField(max_digits=12, decimal_places=2)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Fluxo de Caixa - {self.data} - Saldo: R${self.saldo_final}"
    
    class Meta:
        verbose_name = "Fluxo de Caixa"
        verbose_name_plural = "Fluxos de Caixa"
        ordering = ['-data']

    def save(self, *args, **kwargs):
        self.saldo_final = self.saldo_inicial + self.entradas - self.saidas
        super().save(*args, **kwargs)
