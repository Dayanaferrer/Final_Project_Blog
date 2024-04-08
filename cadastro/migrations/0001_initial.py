# Generated by Django 4.2.11 on 2024-04-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Formulário de cadastro',
                'verbose_name_plural': 'Formulário de cadastros',
                'ordering': ['-data'],
            },
        ),
    ]