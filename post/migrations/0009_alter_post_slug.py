# Generated by Django 4.2.11 on 2024-04-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0008_alter_comentario_nome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]
