/home/igor/Área de Trabalho/ProjetoSD/staticfiles
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminBlackAdminblacksetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    sidebar_background = models.CharField(max_length=20)
    dark_mode = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_black_adminblacksetting'


class AdminToolsDashboardPreferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField()
    dashboard_id = models.CharField(max_length=100)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_tools_dashboard_preferences'
        unique_together = (('user', 'dashboard_id'),)


class AdminToolsMenuBookmark(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_tools_menu_bookmark'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorias(models.Model):
    categoriaid = models.AutoField(db_column='categoriaID', primary_key=True)  # Field name made lowercase.
    nomecategoria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Clientes(models.Model):
    clienteid = models.AutoField(db_column='clienteID', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estadoid = models.IntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(max_length=10, blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.CharField(max_length=10, blank=True, null=True)
    senha = models.CharField(max_length=10, blank=True, null=True)
    nivel = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Departamentos(models.Model):
    departamentoid = models.AutoField(db_column='departamentoID', primary_key=True)  # Field name made lowercase.
    nomedepartamento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estados(models.Model):
    estadoid = models.AutoField(db_column='estadoID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=20, blank=True, null=True)
    sigla = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados'


class Fornecedores(models.Model):
    fornecedorid = models.AutoField(db_column='fornecedorID', primary_key=True)  # Field name made lowercase.
    nomefornecedor = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estadoid = models.IntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    ddd = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedores'


class FornecedoresContatos(models.Model):
    contatoid = models.AutoField(db_column='contatoID', primary_key=True)  # Field name made lowercase.
    fornecedorid = models.IntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    departamentoid = models.IntegerField(db_column='departamentoID', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedores_contatos'


class Franquias(models.Model):
    franquiaid = models.AutoField(db_column='franquiaID', primary_key=True)  # Field name made lowercase.
    nomegerente = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estadoid = models.IntegerField(db_column='estadoID')  # Field name made lowercase.
    telefone = models.CharField(max_length=15, blank=True, null=True)
    dataabertura = models.DateField()
    faturamento = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'franquias'


class Pedidos(models.Model):
    pedidoid = models.AutoField(db_column='pedidoID', primary_key=True)  # Field name made lowercase.
    clienteid = models.IntegerField(db_column='clienteID')  # Field name made lowercase.
    transportadoraid = models.IntegerField(db_column='transportadoraID', blank=True, null=True)  # Field name made lowercase.
    data_pedido = models.DateField()
    data_saida = models.DateField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    status_pedido = models.IntegerField()
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    conhecimento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class PedidosItem(models.Model):
    pedidoid = models.IntegerField(db_column='pedidoID', blank=True, null=True)  # Field name made lowercase.
    produtoid = models.IntegerField(db_column='produtoID', blank=True, null=True)  # Field name made lowercase.
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade = models.SmallIntegerField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pedidos_item'


class PedidosStatus(models.Model):
    statusid = models.AutoField(db_column='statusID', primary_key=True)  # Field name made lowercase.
    nomestatus = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pedidos_status'


class Produtos(models.Model):
    produtoid = models.AutoField(db_column='produtoID', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    codigobarra = models.CharField(max_length=15, blank=True, null=True)
    tempoentrega = models.IntegerField(blank=True, null=True)
    precorevenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    imagemgrande = models.CharField(max_length=100)
    imagempequena = models.CharField(max_length=100)
    fornecedorid = models.IntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    categoriaid = models.IntegerField(db_column='categoriaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtos'


class ProdutosClientes(models.Model):
    produtoid = models.AutoField(db_column='produtoID', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    codigobarra = models.CharField(max_length=15, blank=True, null=True)
    tempoentrega = models.IntegerField(blank=True, null=True)
    precorevenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    imagemgrande = models.CharField(max_length=100)
    imagempequena = models.CharField(max_length=100)
    descontinuado = models.IntegerField(blank=True, null=True)
    fornecedorid = models.IntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    categoriaid = models.IntegerField(db_column='categoriaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtos_clientes'


class Transportadoras(models.Model):
    transportadoraid = models.AutoField(db_column='transportadoraID', primary_key=True)  # Field name made lowercase.
    nometransportadora = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estadoid = models.IntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(max_length=10, blank=True, null=True)
    cnpj = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportadoras'
