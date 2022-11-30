from django import forms
from pycep_correios.client import WebService, get_address_from_cep

from inicial.models import Estados
from inicial.validators import (validade_NumeroEndereco, validadeTelefone, validarEmailCli, validarEmailCliUpd, validarEmailForn, validarEmailFornUpd,
                                validarUserCliente, validarUserClienteUpdate,
                                validarUserForn, validate_cep, validate_nomeCliente,
                                validate_nomeClienteUpdate,
                                validate_nomeFornecedor,
                                validate_nomeFornecedorUpdate)


class AdicionarClienteIniForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AdicionarClienteIniForm, self).__init__(*args, **kwargs)
        self.fields['ddd'] = forms.IntegerField(max_value=99, min_value=11)

    nomecompleto = forms.CharField(
        required=True,
        label='Nome Completo',
        validators=[validate_nomeCliente],
    )

    cep = forms.CharField(
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    ddd = forms.CharField(
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        required=True,
        label='Telefone',
        validators=[validadeTelefone]
    )

    email = forms.EmailField(
        required=True,
        label='E-mail',
        validators=[validarEmailCli]
    )


class AdicionarClienteForm(forms.Form):
    def __init__(self, data, *args, **kwargs):
        super(AdicionarClienteForm, self).__init__(*args, **kwargs)
        campos = get_address_from_cep(data.get('cep'), webservice=WebService.VIACEP)
        self.fields['nomecompleto'].initial = data.get('nomecompleto')
        self.fields['cep'].initial = campos.get('cep')
        self.fields['ddd'].initial = data.get('ddd')
        self.fields['telefone'].initial = data.get('telefone')
        self.fields['email'].initial = data.get('email')
        self.fields['endereco'].initial = campos.get('logradouro')
        self.fields['complemento'].initial = campos.get('complemento')
        try:
            self.fields['numero'].initial = int(campos.get('gia'))
        except (campos.get("gia") is None):
            pass
        self.fields['cidade'].initial = campos.get('cidade')
        estado = Estados.objects.get(sigla__icontains=campos.get('uf'))
        self.fields['estado'].initial = estado.nome
        self.fields['senha'] = forms.CharField(widget=forms.PasswordInput)

    nomecompleto = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome Completo',
        validators=[],
    )

    endereco = forms.CharField(
        required=True,
        label='Endereco',
        validators=[],
    )

    complemento = forms.CharField(
        required=True,
        label='Complemento',
        validators=[],
    )

    numero = forms.CharField(
        required=True,
        label='Número',
        validators=[validade_NumeroEndereco],
    )

    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Cidade',
        validators=[],
    )

    estado = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Estado',
        validators=[],
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    ddd = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Telefone',
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='E-mail',
    )

    usuario = forms.CharField(
        required=True,
        label='Usuário para acesso',
        validators=[validarUserCliente]
    )

    senha = forms.CharField(
        required=True,
        label='Senha',
    )


class AlterarClienteIniForm(forms.Form):
    def __init__(self, atual, *args, **kwargs):
        super(AlterarClienteIniForm, self).__init__(*args, **kwargs)
        self.fields['ddd'] = forms.IntegerField(max_value=99, min_value=11)
        self.fields['nomecompleto'].initial = atual.nomecompleto
        self.fields['cep'].initial = atual.cep
        self.fields['ddd'].initial = int(atual.ddd)
        self.fields['telefone'].initial = atual.telefone
        self.fields['email'].initial = atual.email

    nomecompleto = forms.CharField(
        required=True,
        label='Nome Completo',
        validators=[validate_nomeClienteUpdate],
    )

    cep = forms.CharField(
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    ddd = forms.CharField(
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        required=True,
        label='Telefone',
        validators=[validadeTelefone]
    )

    email = forms.EmailField(
        required=True,
        label='E-mail',
        validators=[validarEmailCliUpd]
    )


class AlterarClienteForm(forms.Form):
    def __init__(self, data, atual, *args, **kwargs):
        super(AlterarClienteForm, self).__init__(*args, **kwargs)
        campos = get_address_from_cep(data.get('cep'), webservice=WebService.VIACEP)
        estado = Estados.objects.get(sigla__icontains=campos.get("uf"))
        self.fields['nomecompleto'].initial = data.get('nomecompleto')
        self.fields['cep'].initial = campos.get('cep')
        self.fields['ddd'].initial = data.get('ddd')
        self.fields['telefone'].initial = data.get('telefone')
        self.fields['email'].initial = data.get('email')
        self.fields['endereco'].initial = campos.get('logradouro')
        self.fields['complemento'].initial = campos.get('complemento')
        try:
            self.fields['numero'].initial = int(campos.get('gia'))
        except (campos.get("gia") is None):
            pass
        self.fields['cidade'].initial = campos.get('cidade')
        self.fields['estado'].initial = estado.nome
        self.fields['usuario'].initial = atual.usuario
        self.fields['senha'].initial = atual.senha
        self.fields['senha'] = forms.CharField(widget=forms.PasswordInput)

    nomecompleto = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome Completo',
        validators=[],
    )

    endereco = forms.CharField(
        required=True,
        label='Endereco',
        validators=[],
    )

    complemento = forms.CharField(
        required=True,
        label='Complemento',
        validators=[],
    )

    numero = forms.CharField(
        required=True,
        label='Número',
        validators=[validade_NumeroEndereco],
    )

    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Cidade',
        validators=[],
    )

    estado = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Estado',
        validators=[],
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    ddd = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Telefone',
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='E-mail',
    )

    usuario = forms.CharField(
        required=True,
        label='Usuário para acesso',
        validators=[validarUserClienteUpdate]
    )

    senha = forms.CharField(
        required=True,
        label='Senha',
    )


class AdicionarFornecedorIniForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AdicionarFornecedorIniForm, self).__init__(*args, **kwargs)
        self.fields['ddd'] = forms.IntegerField(max_value=99, min_value=11)

    nomefornecedor = forms.CharField(
        required=True,
        label='Nome do Fornecedor',
        validators=[validate_nomeFornecedor],
    )

    cep = forms.CharField(
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    ddd = forms.CharField(
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        required=True,
        label='Telefone',
        validators=[validadeTelefone]
    )

    email = forms.EmailField(
        required=True,
        label='E-mail',
        validators=[validarEmailForn]
    )


class AdicionarFornecedorForm(forms.Form):
    def __init__(self, dados, *args, **kwargs):
        super(AdicionarFornecedorForm, self).__init__(*args, **kwargs)
        campos = get_address_from_cep(dados.get('cep'), webservice=WebService.VIACEP)
        estado = Estados.objects.get(sigla__icontains=campos.get('uf'))
        self.fields['nomefornecedor'].initial = dados.get('nomefornecedor')
        self.fields['cep'].initial = campos.get('cep')
        self.fields['endereco'].initial = campos.get('logradouro')
        self.fields['cidade'].initial = campos.get('cidade')
        self.fields['estado'].initial = estado.nome
        self.fields['ddd'].initial = dados.get('ddd')
        self.fields['telefone'].initial = dados.get('telefone')
        self.fields['email'].initial = dados.get('email')
        self.fields['senha'] = forms.CharField(widget=forms.PasswordInput)

    nomefornecedor = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome do Fornecedor',
        validators=[validate_nomeFornecedor],
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    endereco = forms.CharField(
        required=True,
        label='Endereco',
        validators=[],
    )

    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Cidade',
        validators=[],
    )

    estado = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Estado',
        validators=[],
    )

    ddd = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Telefone',
        validators=[validadeTelefone]
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='E-mail',
    )

    usuario = forms.CharField(
        required=True,
        label='Usuário para acesso',
        validators=[validarUserForn]
    )

    senha = forms.CharField(
        required=True,
        label='Senha',
    )


class AlterarFornecedorIniForm(forms.Form):
    def __init__(self, dados, *args, **kwargs):
        super(AlterarFornecedorIniForm, self).__init__(*args, **kwargs)
        self.fields['ddd'] = forms.IntegerField(max_value=99, min_value=11)
        self.fields['nomefornecedor'].initial = dados.nomefornecedor
        self.fields['cep'].initial = dados.cep
        self.fields['ddd'].initial = int(dados.ddd)
        self.fields['telefone'].initial = dados.telefone
        self.fields['email'].initial = dados.email

    nomefornecedor = forms.CharField(
        required=True,
        label='Nome do Fornecedor',
        validators=[validate_nomeFornecedorUpdate],
    )

    cep = forms.CharField(
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    ddd = forms.CharField(
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        required=True,
        label='Telefone',
        validators=[validadeTelefone]
    )

    email = forms.EmailField(
        required=True,
        label='E-mail',
        validators=[validarEmailFornUpd]
    )


class AlterarFornecedorForm(forms.Form):
    def __init__(self, dados, atual, *args, **kwargs):
        super(AlterarFornecedorForm, self).__init__(*args, **kwargs)
        campos = get_address_from_cep(dados.get('cep'), webservice=WebService.VIACEP)
        estado = Estados.objects.get(sigla__icontains=campos.get('uf'))
        self.fields['nomefornecedor'].initial = dados.get('nomefornecedor')
        self.fields['cep'].initial = campos.get('cep')
        self.fields['endereco'].initial = campos.get('logradouro')
        self.fields['cidade'].initial = campos.get('cidade')
        self.fields['estado'].initial = estado.nome
        self.fields['ddd'].initial = dados.get('ddd')
        self.fields['telefone'].initial = dados.get('telefone')
        self.fields['usuario'].initial = atual.usuario
        self.fields['email'].initial = dados.get('email')
        self.fields['senha'].initial = atual.senha
        self.fields['senha'] = forms.CharField(widget=forms.PasswordInput)

    nomefornecedor = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome do Fornecedor',
        validators=[validate_nomeFornecedorUpdate],
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    endereco = forms.CharField(
        required=True,
        label='Endereco',
        validators=[],
    )

    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Cidade',
        validators=[],
    )

    estado = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Estado',
        validators=[],
    )

    ddd = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='DDD',
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Telefone',
        validators=[validadeTelefone]
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='E-mail',
        validators=[validarEmailFornUpd]
    )

    usuario = forms.CharField(
        required=True,
        label='Usuário para acesso',
    )

    senha = forms.CharField(
        required=True,
        label='Senha',
    )
