# Generated by Django 2.1.1 on 2018-09-17 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabeleireira', '0002_auto_20180917_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabeleireira_servico',
            name='cabeleireira',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cabeleireira.Cabeleireira'),
        ),
        migrations.AlterField(
            model_name='cabeleireira_servico',
            name='servico',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Servico.Servico'),
        ),
    ]