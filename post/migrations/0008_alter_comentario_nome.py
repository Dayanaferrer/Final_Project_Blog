# Generated by Django 4.2.11 on 2024-04-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0007_comentario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="nome",
            field=models.CharField(
                choices=[("Anônimo", "Anônimo"), ("Logado", "Logado")], max_length=150
            ),
        ),
    ]