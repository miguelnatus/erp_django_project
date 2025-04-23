from django import forms
from .models import Produto, Movimentacao, Fornecedor

class ProdutoForm(forms.ModelForm):
    """
    Formulário para criação e edição de produtos,
    apenas com os campos que existem em Produto.
    """
    class Meta:
        model = Produto
        fields = [
            'nome',
            'descricao',
            'codigo',
            'categoria',
            'preco_custo',
            'preco_venda',
            'estoque_atual',
            'estoque_minimo',
            'unidade_medida',
            'ativo',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'preco_custo': forms.NumberInput(attrs={'step': '0.01'}),
            'preco_venda': forms.NumberInput(attrs={'step': '0.01'}),
        }

class FornecedorForm(forms.ModelForm):
    """
    Formulário para criação e edição de fornecedores,
    apenas com os campos que existem em Fornecedor.
    """
    class Meta:
        model = Fornecedor
        fields = [
            'nome',
            'cnpj',
            'email',
            'telefone',
            'endereco',
            'contato',
        ]
        # não há widgets adicionais aqui

class MovimentacaoForm(forms.ModelForm):
    """
    Formulário para registro de movimentações de estoque.
    """
    class Meta:
        model = Movimentacao
        fields = [
            'produto',
            'tipo',
            'quantidade',
            'data',
            'responsavel',
            'observacao',
        ]
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }
