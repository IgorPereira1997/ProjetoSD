from inicial.models import Estados
from listar_transportadoras.models import Transportadoras
from inicial.validators import transportadora_uso, validate_cep, validate_cnpj, validate_cnpjUpdate, validate_nomeTransportadora, validate_nomeTransportadoraUpdate
from django import forms


class AdicionarTransportadoraForm(forms.Form):
    def __init__(self, estados_choices, detalhes, *args, **kwargs):
        super(AdicionarTransportadoraForm, self).__init__(*args, **kwargs)
        self.fields['estados'].choices = estados_choices
        self.fields['endereco'].initial = detalhes.get('endereco')
        self.fields['estados'].initial = detalhes.get('estado')
        self.fields['nometransportadora'].initial = detalhes.get('nome')
        self.fields['cep'].initial = detalhes.get('cep')
        self.fields['telefone'].initial = detalhes.get('telefone')
        self.fields['cnpj'].initial = detalhes.get('cnpj')
        self.fields['cidade'].initial = detalhes.get('cidade')

    nometransportadora = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome',
        validators=[validate_nomeTransportadora],
    )

    endereco = forms.CharField(
        required=True,
        label='Endereço',
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    estados = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label="Estado",
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Telefone',
    )

    cnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CNPJ',
    )

    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label='Cidade',
    )


class AdicionarTransportadoraIniForm(forms.Form):
    nometransportadora = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome da Transportadora'}
        ),
        required=True,
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'CEP'}
        ),
        required=True,
        validators=[validate_cep],
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Telefone'}
        ),
        required=True,
    )

    cnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'CNPJ'}
        ),
        required=True,
        validators=[validate_cnpj],
    )


class AlterarTransportadoraIniForm(forms.Form):
    def __init__(self, detalhes, *args, **kwargs):
        super(AlterarTransportadoraIniForm, self).__init__(*args, **kwargs)
        if detalhes:
            self.fields['nometransportadora'].initial = detalhes.nometransportadora
            self.fields['cep'].initial = detalhes.cep
            self.fields['telefone'].initial = detalhes.telefone
            self.fields['cnpj'].initial = detalhes.cnpj

    nometransportadora = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nome da Transportadora'}
        ),
        required=True,
        validators=[validate_nomeTransportadoraUpdate]
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'CEP'}
        ),
        required=True,
        validators=[validate_cep],
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Telefone'}
        ),
        required=True,
    )

    cnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'CNPJ'}
        ),
        required=True,
        validators=[validate_cnpjUpdate],
    )


class AlterarTransportadoraForm(forms.Form):
    def __init__(self, estados_choices, detalhes, *args, **kwargs):
        super(AlterarTransportadoraForm, self).__init__(*args, **kwargs)
        self.fields['estados'].choices = estados_choices
        self.fields['endereco'].initial = detalhes.get('endereco')
        self.fields['estados'].initial = detalhes.get('estado')
        self.fields['nometransportadora'].initial = detalhes.get('nome')
        self.fields['cep'].initial = detalhes.get('cep')
        self.fields['telefone'].initial = detalhes.get('telefone')
        self.fields['cnpj'].initial = detalhes.get('cnpj')
        self.fields['cidade'].initial = detalhes.get('cidade')

    nometransportadora = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome',
    )

    endereco = forms.CharField(
        required=True,
        label='Endereço',
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CEP',
    )

    estados = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label="Estado",
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Telefone',
    )

    cnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CNPJ',
    )

    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label='Cidade',
    )


class DeletarTransportadoraForm(forms.Form):
    def __init__(self, id, *args, **kwargs):
        super(DeletarTransportadoraForm, self).__init__(*args, **kwargs)
        transp = Transportadoras.objects.get(transportadoraid__exact=id)
        estado = Estados.objects.get(estadoid__exact=transp.estadoid)
        self.fields['estados'].choices = (estado.sigla, estado.nome)
        self.fields['endereco'].initial = transp.endereco
        self.fields['estados'].initial = estado.nome
        self.fields['nometransportadora'].initial = transp.nometransportadora
        self.fields['cep'].initial = transp.cep
        self.fields['telefone'].initial = transp.telefone
        self.fields['cnpj'].initial = transp.cnpj
        self.fields['cidade'].initial = transp.cidade
        self.fields['id'].initial = id

    nometransportadora = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome',
    )

    endereco = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label='Endereço',
    )

    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label='CEP',
    )

    estados = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label="Estado",
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label='Telefone',
    )

    cnpj = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label='CNPJ',
    )

    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={'readonly': True}
        ),
        label='Cidade',
    )

    id = forms.IntegerField(
        widget=forms.HiddenInput(),
        validators=[transportadora_uso],
    )
