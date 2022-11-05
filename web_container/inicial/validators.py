from login.models import Clientes, Fornecedores
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pycep_correios import get_address_from_cep, WebService
from listar_produtos.models import Produtos
from listar_transportadoras.models import Transportadoras
from gerenciar_pedidos.models import Pedidos


def validate_float(value):
    value_test = value.replace(',', '.')
    try:
        value_test = float(value_test)
    except (value_test.isnumeric() is False):
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
    except (value.isnumeric() is False):
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
    except (value.isnumeric() is False):
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
    except (get_address_from_cep(value, webservice=WebService.VIACEP) is None):
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
    except (value_test.isnumeric() is False):
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
        return value_int


def validate_cnpjUpdate(value):
    try:
        value_test = value.replace('.', '')
        value_test = value_test.replace('/', '')
        value_test = value_test.replace('-', '')
        value_int = int(value_test)
    except (value_test.isnumeric() is False):
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


def validate_nomeCliente(value):
    if Clientes.objects.filter(nomecompleto__icontains=value).count() != 0:
        raise ValidationError(
            _('O(a) Cliente já existe! Se quiser modificá-lo(a) vá em "Editar Perfil"!')
        )
    else:
        return value


def validate_nomeClienteUpdate(value):
    if Clientes.objects.filter(nomecompleto__icontains=value).count() > 1:
        raise ValidationError(
            _('O(a) cliente já existe! Se quiser modificá-lo(a) vá em "Editar Perfil"!')
        )
    else:
        return value


def validate_nomeFornecedor(value):
    if Fornecedores.objects.filter(nomefornecedor__icontains=value).count() != 0:
        raise ValidationError(
            _('O(a) fornecedor(a) já existe! Se quiser modificá-lo(a) vá em "Editar Perfil"!')
        )
    else:
        return value


def validate_nomeFornecedorUpdate(value):
    if Clientes.objects.filter(nomecompleto__icontains=value).count() > 1:
        raise ValidationError(
            _('O(a) fornecedor(a) já existe! Se quiser modificá-lo(a) vá em "Editar Perfil"!')
        )
    else:
        return value


def validade_NumeroEndereco(value):
    try:
        valor_int = int(value)
    except (value.isnumeric() is False):
        raise ValidationError(
            _('Não foi fornecido um número!')
        )
    if valor_int < 1:
        raise ValidationError(
            _('O número fornecido não é válido!')
        )
    else:
        return value


def validarUserCliente(valor):
    if Clientes.objects.filter(usuario__iexact=valor):
        raise ValidationError(
            _('Usuário não disponível!')
        )
    return valor


def validarUserClienteUpdate(valor):
    if Clientes.objects.filter(usuario__iexact=valor):
        try:
            Clientes.objects.get(usuario__iexact=valor)
            return valor
        except Clientes.objects.get(usuario__iexact=valor).DoesNotExist:
            raise ValidationError(
                _('Usuário não disponível!')
            )
    return valor


def validarUserForn(valor):
    if Fornecedores.objects.filter(usuario__iexact=valor):
        raise ValidationError(
            _('Usuário não disponível!')
        )
    return valor


def validarUserFornUpdate(valor):
    if Fornecedores.objects.filter(usuario__iexact=valor):
        try:
            Fornecedores.objects.get(usuario__iexact=valor)
            return valor
        except Fornecedores.objects.get(usuario__iexact=valor).DoesNotExist:
            raise ValidationError(
                _('Usuário não disponível!')
            )
    return valor


def validadeTelefone(value):
    valor_Preformatado = value.replace('-', '')
    try:
        valor_formatado = int(valor_Preformatado)
    except (valor_Preformatado.isnumeric() is False):
        raise ValidationError(
            _('Não foi fornecido um telefone!')
        )
    if valor_formatado < 10000000 or valor_formatado >= 1000000000:
        raise ValidationError(
            _('Telefone fornecido é inválido!')
        )
    else:
        return valor_formatado


def transportadora_uso(value):
    if Pedidos.objects.filter(transportadoraid__exact=value):
        flag = False
        pedidos = Pedidos.objects.filter(transportadoraid__exact=value)
        for pedido in pedidos:
            if pedido.status_pedido != 7 or pedido.status_pedido != 3 or pedido.status_pedido != 4:
                flag = True
                break
        if flag:
            raise ValidationError(
                _('A transportadora possui pedidos em andamento, não pode ser deletada!')
            )
        else:
            return value
    else:
        return value


def validarEmailCli(value):
    if Clientes.objects.filter(email__iexact=value):
        raise ValidationError(
            _('Email já está em uso!')
        )
    return value


def validarEmailForn(value):
    if Fornecedores.objects.filter(email__iexact=value):
        raise ValidationError(
            _('Email já está em uso!')
        )
    return value


def validarEmailCliUpd(value):
    if Clientes.objects.filter(email__iexact=value):
        try:
            Clientes.objects.get(email__iexact=value)
            return value
        except Clientes.objects.get(email__iexact=value).DoesNotExist:
            raise ValidationError(
                _('Email já está em uso!')
            )


def validarEmailFornUpd(value):
    if Fornecedores.objects.filter(email__iexact=value):
        try:
            Fornecedores.objects.get(email__iexact=value)
            return value
        except (Fornecedores.objects.get(email__iexact=value).DoesNotExist):
            raise ValidationError(
                _('Email já está em uso!')
            )


def validarRecuperarCli(value):
    if Clientes.objects.filter(email__iexact=value):
        return value
    else:
        raise ValidationError(
            _('Email não cadastrado')
        )


def validarRecuperarForn(value):
    if Fornecedores.objects.filter(email__iexact=value):
        return value
    else:
        raise ValidationError(
            _('Email não cadastrado')
        )
