# Generated by Django 4.0.4 on 2022-07-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0011_remove_descripcion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='descripcion',
            name='imagen',
            field=models.ImageField(default=1, upload_to='descripcion_image'),
            preserve_default=False,
        ),
    ]
