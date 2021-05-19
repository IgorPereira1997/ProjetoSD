from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pycep_correios import get_address_from_cep, WebService
from listar_produtos.models import Produtos
from listar_transportadoras.models import Transportadoras

def validate_float(value):
    value_test = value.replace(',', '.')
    try: 
        value_test = float(value_test)
    except:
        raise ValidationError(
            _('%(value)s não é um número!'),
            params={'value': value},
        )
    if value_test <= 0:
            raise ValidationError(
                _('%(value)s não é um número válido!'),
                params={'value': value},
            )
    else:
        return value


def validate_barcode(value):
    try: 
        value_str = int(value)
    except:
        raise ValidationError(
            _('%(value)s não é um código de barras!'),
            params={'value': value},
        )
    if value_str > 10000000000000 or value_str < 100000000000 or (value_str < 1000000000000 and value[0] != '0'):
        raise ValidationError(
            _('%(value)s não é um código de barra válido!'),
            params={'value': value},
        )
    else:    
        if Produtos.objects.filter(codigobarra__exact=value):
            raise ValidationError(
                _('O código de barra já existe!'),
                params={'value': value},
            )
        else:
            return value
    
def validate_barcodeUpdate(value):
    try: 
        value_str = int(value)
    except:
        raise ValidationError(
            _('%(value)s não é um código de barras!'),
            params={'value': value},
        )
    if value_str > 10000000000000 or value_str < 100000000000 or (value_str < 1000000000000 and value[0] != '0'):
        raise ValidationError(
            _('%(value)s não é um código de barra válido!'),
            params={'value': value},
        )
    else:    
        if Produtos.objects.filter(codigobarra__icontains=value).count() > 1:
            raise ValidationError(
                _('O código de barra já existe!'),
                params={'value': value},
            )
        else:
            return value

def validate_cep(value):
    try:
        endereco = get_address_from_cep(value, webservice=WebService.VIACEP)
        return endereco
    except:
        raise ValidationError(
            _('%(value)s não é um CEP válido!'),
            params={'value': value},
        )


def validate_cnpj(value):
    try:
        value_test = value.replace('.', '')
        value_test = value_test.replace('/', '')
        value_test = value_test.replace('-', '')
        value_int = int(value_test)
    except:
        raise ValidationError(
            _('%(value)s não é um CNPJ válido'),
            params={'value': value},
        )
    if value_int >= 1000000000000000 or value_int < 1000000000000 or (value_int < 1000000000000 and value_int[0] != '0'):
        raise ValidationError(
            _('%(value)s não é um CNPJ válido'),
            params={'value': value},
        )
    else:
        if Transportadoras.objects.filter(cnpj__exact=value):
            raise ValidationError(
                _('O CNPJ já existe!'),
                params={'value': value},
            )
        return value

def validate_cnpjUpdate(value):
    try:
        value_test = value.replace('.', '')
        value_test = value_test.replace('/', '')
        value_test = value_test.replace('-', '')
        value_int = int(value_test)
    except:
        raise ValidationError(
            _('%(value)s não é um CNPJ válido'),
            params={'value': value},
        )
    if value_int >= 1000000000000000 or value_int < 1000000000000 or (value_int < 1000000000000 and value_int[0] != '0'):
        raise ValidationError(
            _('%(value)s não é um CNPJ válido'),
            params={'value': value},
        )
    else:
        if Transportadoras.objects.filter(cnpj__exact=value_int).count() > 1:
            raise ValidationError(
                _('O CNPJ já existe!'),
                params={'value': value},
            )
        return value_int


def validate_nomeProduto(value):
    if Produtos.objects.filter(nomeproduto__exact=value):
        raise ValidationError(
            _('O produto já existe! Se quiser modificá-lo vá em "Atualizar Produto" na página "Detalhes"!')
        )
    else:
        return value

def validate_nomeProdutoUpdate(value):
    if Produtos.objects.filter(nomeproduto__icontains=value).count() > 1:
        raise ValidationError(
            _('O produto já existe! Se quiser modificá-lo vá em "Atualizar Produto" na página "Detalhes"!')
        )
    else:
        return value


def validate_nomeTransportadora(value):
    if Transportadoras.objects.filter(nometransportadora__exact=value):
        raise ValidationError(
            _('A transportadora já existe! Se quiser modificá-la vá em "Atualizar" no menu inicial!')
        )
    else:
        return value

def validate_nomeTransportadoraUpdate(value):
    if Transportadoras.objects.filter(nometransportadora__icontains=value).count() > 1:
        raise ValidationError(
            _('A transportadora já existe! Se quiser modificá-la vá em "Atualizar" no menu inicial!')
        )
    else:
        return value
