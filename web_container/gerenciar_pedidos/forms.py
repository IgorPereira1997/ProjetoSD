from django import forms


class PedidoForm(forms.Form):
    def __init__(self, estoque_total, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['estoque'] = forms.IntegerField(
            max_value=estoque_total, min_value=1)
    estoque = forms.IntegerField(required=True,
                                 label='Selecione a quantidade',)


class TransportadoraPedidoForm(forms.Form):
    def __init__(self, transp, *args, **kwargs):
        super(TransportadoraPedidoForm, self).__init__(*args, **kwargs)
        self.fields['transportadora'].choices = transp

    transportadora = forms.ChoiceField(choices=(),
                                       required=True,
                                       label="Escolha a Transportadora",)


class ModificarPedidoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ModificarPedidoForm, self).__init__(*args, **kwargs)

    statuspedido = forms.ChoiceField(choices=(),
                                     required=True,
                                     label="Escolha o novo Status",)
