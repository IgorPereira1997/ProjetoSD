from inicial.validators import validarRecuperarCli, validarRecuperarForn
from django import forms


class RecuperarSenhaCliForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RecuperarSenhaCliForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        required=True,
        label='E-mail',
        validators=[validarRecuperarCli]
    )


class RecuperarSenhaFornForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RecuperarSenhaFornForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        required=True,
        label='E-mail',
        validators=[validarRecuperarForn]
    )


class RecuperarSenhaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RecuperarSenhaForm, self).__init__(*args, **kwargs)
        self.fields['novasenha'] = forms.CharField(widget=forms.PasswordInput)

    novasenha = forms.CharField(
        label="Nova Senha",
        required=True,
    )
