# Generated by Django 2.1.1 on 2018-09-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Servico', '0004_auto_20180916_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Nome')),
                ('descrição', models.TextField(blank=True, verbose_name='Descrição')),
                ('valor_minimo', models.CharField(max_length=4, verbose_name='Valor_minimo')),
                ('valor_maximo', models.CharField(max_length=4, verbose_name='Valor_maximo')),
                ('imagem', models.CharField(blank=True, max_length=1000, verbose_name='Imagem')),
                ('valor_desconto', models.IntegerField(blank=True, default=0, verbose_name='Valor Desconto')),
                ('servico', models.ManyToManyField(to='Servico.Servico')),
            ],
        ),
    ]
