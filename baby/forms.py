from django import forms
from .models import Produto, PropostaTroca, Mensagem, Categoria, Marca


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'titulo', 'descricao', 'categoria',
            'tamanho_fralda', 'tamanho_roupa',
            'para_bebe', 'para_mae',
            'condicao', 'valor_estimado', 'preferencias_troca',
            'imagem_principal',
            'cidade', 'estado'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none',
                'placeholder': 'Ex: Carrinho de Bebê Chicco Lite Way'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 min-h-[160px] focus:ring-2 focus:ring-primary/50 focus:outline-none',
                'placeholder': 'Descreva o estado do item, tempo de uso, acessórios inclusos...'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none'
            }),
            'valor_estimado': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 pl-10 focus:ring-2 focus:ring-primary/50 focus:outline-none',
                'placeholder': '0,00',
                'step': '0.01'
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 pl-11 focus:ring-2 focus:ring-primary/50 focus:outline-none',
                'placeholder': 'Ex: São Paulo'
            }),
            'preferencias_troca': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none',
                'placeholder': 'O que você aceita na troca?',
                'rows': 3
            }),
            'condicao': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none'
            }),
            'tamanho_fralda': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none'
            }),
            'tamanho_roupa': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 bg-slate-50 focus:ring-2 focus:ring-primary/50 focus:outline-none'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(ativa=True)


class PropostaTrocaForm(forms.ModelForm):
    class Meta:
        model = PropostaTroca
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-primary/50 focus:outline-none',
                'placeholder': 'Olá! Gostaria de trocar meu produto pelo seu...',
                'rows': 4
            })
        }


class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['conteudo']
        widgets = {
            'conteudo': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-slate-200 focus:ring-2 focus:ring-primary/50 focus:outline-none',
                'placeholder': 'Digite sua mensagem...',
                'rows': 3
            })
        }
