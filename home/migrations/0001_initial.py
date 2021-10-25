# Generated by Django 3.2.7 on 2021-10-25 19:35

from django.db import migrations, models
import home.models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('ingrediente', models.CharField(max_length=500, verbose_name='Ingrediente')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('imagem', stdimage.models.StdImageField(upload_to=home.models.get_file_path, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Prato',
                'verbose_name_plural': 'Pratos',
            },
        ),
    ]