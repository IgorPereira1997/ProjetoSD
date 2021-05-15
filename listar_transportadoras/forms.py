from inicial.validators import validate_cep, validate_cnpj, validate_nomeTransportadora
from django import forms
from inicial.models import Estados

class AdicionarTransportadoraForm(forms.Form):
    def __init__(self, estados_choices, detalhes, *args, **kwargs):
        super(AdicionarTransportadoraForm, self).__init__(*args, **kwargs)
        self.fields['estados'].choices            = estados_choices
        self.fields['endereco'].initial           = detalhes.get('endereco')
        self.fields['estados'].initial            = detalhes.get('estado')
        self.fields['nometransportadora'].initial = detalhes.get('nome')
        self.fields['cep'].initial                = detalhes.get('cep')
        self.fields['telefone'].initial           = detalhes.get('telefone')
        self.fields['cnpj'].initial               = detalhes.get('cnpj')
        self.fields['cidade'].initial             = detalhes.get('cidade')

    nometransportadora = forms.CharField(
        widget= forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Nome da Transportadora',
        validators=[validate_nomeTransportadora],
    )

    endereco = forms.CharField(
        required=True,
        label='Endereço',
    )

    cep = forms.CharField(
        widget= forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CEP',
        validators=[validate_cep],
    )

    estados = forms.CharField(
        widget= forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label="Estado",
    )
    
    telefone = forms.CharField(
        widget= forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='Telefone',
    )

    cnpj = forms.CharField(
        widget= forms.TextInput(
            attrs={'readonly': True}
        ),
        required=True,
        label='CNPJ',
        validators=[validate_cnpj],
    )

    cidade = forms.CharField(
        widget= forms.TextInput(
            attrs={'readonly': True}
        ),
        label='Cidade',
    )

class AdicionarTransportadoraIniForm(forms.Form):
    def __init__(self, detalhes ,*args, **kwargs):
        super(AdicionarTransportadoraIniForm, self).__init__(*args, **kwargs)
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
    )

    cep = forms.CharField(
        widget= forms.TextInput(
            attrs={'placeholder': 'CEP'}
        ),
        required=True,
        validators=[validate_cep],
    )
    
    telefone = forms.CharField(
        widget= forms.TextInput(
            attrs={'placeholder': 'Telefone'}
        ),
        required=True,
    )

    cnpj = forms.CharField(
        widget= forms.TextInput(
            attrs={'placeholder': 'CNPJ'}
        ),
        required=True,
        validators=[validate_cnpj],
    )