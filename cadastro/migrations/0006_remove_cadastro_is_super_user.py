# Generated by Django 4.2.11 on 2024-04-10 18:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cadastro", "0005_remove_cadastro_usuario"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cadastro",
            name="is_super_user",
        ),
    ]