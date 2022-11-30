from inicial.validators import validate_barcode, validate_barcodeUpdate, validate_float, validate_nomeProduto, validate_nomeProdutoUpdate
from django import forms
from inicial.upload_validator import FileTypeValidator


class AdicionarProdutoForm(forms.Form):
    def __init__(self, forn_choices, cat_choices, entrega_choices, *args, **kwargs):
        super(AdicionarProdutoForm, self).__init__(*args, **kwargs)
        self.fields['fornecedorid'].choices = forn_choices
        self.fields['categoriaid'].choices = cat_choices
        self.fields['tempoentrega'].choices = entrega_choices

    nomeproduto = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome do Produto'}),
        required=True,
        validators=[validate_nomeProduto],
    )

    codigobarra = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Código de Barra'}),
        required=True,
        validators=[validate_barcode],
    )

    descricao = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Descrição do Produto'}),
        required=True,
    )

    tempoentrega = forms.ChoiceField(
        choices=(),
        required=True,
        label="Tempo de Entrega do Produto",
    )

    categoriaid = forms.ChoiceField(
        choices=(),
        required=True,
        label="Categoria do Produto",
    )

    fornecedorid = forms.ChoiceField(
        choices=(),
        required=True,
        label="Fornecedor do Produto",
    )

    precorevenda = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Preço de revenda'}
        ),
        required=True,
        validators=[validate_float],
    )

    precounitario = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Preço Unitário'}),
        required=True,
        validators=[validate_float],
    )

    estoque = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Estoque adquirido'}),
        required=True,
        min_value=1,
    )

    foto_grande = forms.FileField(
        label='Forneça a imagem grande do produto:',
        required=True,
        validators=[FileTypeValidator(allowed_types=['image/*'])],
    )

    foto_pequena = forms.FileField(
        label='Forneça a imagem pequena do produto:',
        required=True,
        validators=[FileTypeValidator(allowed_types=['image/*'])],
    )


class AlterarProdutoForm(forms.Form):
    def __init__(self, forn_choices, cat_choices, entrega_choices, prod, *args, **kwargs):
        super(AlterarProdutoForm, self).__init__(*args, **kwargs)
        self.fields['fornecedorid'].choices = forn_choices
        self.fields['categoriaid'].choices = cat_choices
        self.fields['tempoentrega'].choices = entrega_choices
        self.fields['nomeproduto'].initial = prod.nomeproduto
        self.fields['codigobarra'].initial = prod.codigobarra
        self.fields['descricao'].initial = prod.descricao
        self.fields['tempoentrega'].initial = int(prod.tempoentrega)
        self.fields['categoriaid'].initial = prod.categoriaid
        self.fields['fornecedorid'].initial = prod.fornecedorid
        self.fields['precorevenda'].initial = str(round(prod.precorevenda, 2)).replace('.', ',')
        self.fields['precounitario'].initial = str(round(prod.precounitario, 2)).replace('.', ',')
        self.fields['foto_grande'].initial = prod.imagemgrande
        self.fields['foto_pequena'].initial = prod.imagempequena
        self.fields['estoque'].initial = int(prod.estoque)

    nomeproduto = forms.CharField(
        required=True,
        label="Nome do Produto",
        validators=[validate_nomeProdutoUpdate]
    )

    codigobarra = forms.CharField(
        required=True,
        label="Código de Barra",
        validators=[validate_barcodeUpdate]
    )

    descricao = forms.CharField(
        required=True,
        label="Descrição",
    )

    tempoentrega = forms.ChoiceField(
        choices=(),
        required=True,
        label="Tempo de Entrega do Produto",
    )

    categoriaid = forms.ChoiceField(
        choices=(),
        required=True,
        label="Categoria do Produto",
    )

    fornecedorid = forms.ChoiceField(
        choices=(),
        required=True,
        label="Fornecedor do Produto",
    )

    precorevenda = forms.CharField(
        required=True,
        label='Preço de revenda',
        validators=[validate_float],
    )

    precounitario = forms.CharField(
        required=True,
        label='Preço Unitário',
        validators=[validate_float],
    )

    estoque = forms.IntegerField(
        required=True,
        label='Estoque adquirido',
        min_value=1,
    )

    foto_grande = forms.FileField(
        label='Forneça a imagem grande do produto:',
        required=False,
        validators=[FileTypeValidator(allowed_types=['image/*'])],
    )

    foto_pequena = forms.FileField(
        label='Forneça a imagem pequena do produto:',
        required=False,
        validators=[FileTypeValidator(allowed_types=['image/*'])],
    )


class AlterarProdutoCliForm(forms.Form):
    def __init__(self, forn_choices, cat_choices, entrega_choices, prod, estoque_total, *args, **kwargs):
        super(AlterarProdutoCliForm, self).__init__(*args, **kwargs)
        self.fields['fornecedorid'].choices = forn_choices
        self.fields['categoriaid'].choices = cat_choices
        self.fields['tempoentrega'].choices = entrega_choices
        self.fields['nomeproduto'].initial = prod.nomeproduto
        self.fields['codigobarra'].initial = prod.codigobarra
        self.fields['descricao'].initial = prod.descricao
        self.fields['tempoentrega'].initial = int(prod.tempoentrega)
        self.fields['categoriaid'].initial = prod.categoriaid
        self.fields['fornecedorid'].initial = prod.fornecedorid
        self.fields['precorevenda'].initial = str(round(prod.precorevenda, 2)).replace('.', ',')
        self.fields['precounitario'].initial = str(round(prod.precounitario, 2)).replace('.', ',')
        self.fields['foto_grande'].initial = prod.imagemgrande
        self.fields['foto_pequena'].initial = prod.imagempequena
        self.fields['estoque'] = forms.IntegerField(max_value=estoque_total, min_value=1)
        self.fields['estoque'].initial = int(estoque_total)

    nomeproduto = forms.CharField(
        required=True,
        label="Nome do Produto",
        validators=[validate_nomeProdutoUpdate]
    )

    codigobarra = forms.CharField(
        required=True,
        label="Código de Barra",
        validators=[validate_barcodeUpdate]
    )

    descricao = forms.CharField(
        required=True,
        label="Descrição",
    )

    tempoentrega = forms.ChoiceField(
        choices=(),
        required=True,
        label="Tempo de Entrega do Produto",
    )

    categoriaid = forms.ChoiceField(
        choices=(),
        required=True,
        label="Categoria do Produto",
    )

    fornecedorid = forms.ChoiceField(
        choices=(),
        required=True,
        label="Fornecedor do Produto",
    )

    precorevenda = forms.CharField(
        required=True,
        label='Preço de revenda',
        validators=[validate_float],
    )

    precounitario = forms.CharField(
        required=True,
        label='Preço Unitário',
        validators=[validate_float],
    )

    estoque = forms.IntegerField(
        required=True,
        label='Estoque adquirido',
        min_value=1,
    )

    foto_grande = forms.FileField(
        label='Forneça a imagem grande do produto:',
        required=False,
        validators=[FileTypeValidator(allowed_types=['image/*'])],
    )

    foto_pequena = forms.FileField(
        label='Forneça a imagem pequena do produto:',
        required=False,
        validators=[FileTypeValidator(allowed_types=['image/*'])],
    )
