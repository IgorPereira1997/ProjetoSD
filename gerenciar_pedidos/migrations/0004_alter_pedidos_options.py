# Generated by Django 3.2.3 on 2021-05-25 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciar_pedidos', '0003_alter_pedidositem_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidos',
            options={'managed': True, 'ordering': ('pedidoid', 'data_pedido', 'status_pedido', 'valor_pedido')},
        ),
    ]
