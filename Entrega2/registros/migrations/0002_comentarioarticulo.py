# Generated by Django 3.2.4 on 2021-08-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioArticulo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('art', models.TextField(verbose_name='articulo')),
                ('usuario', models.TextField(verbose_name='Nombre')),
                ('email', models.TextField(verbose_name='Correo')),
                ('tel', models.TextField(verbose_name='Telefono')),
                ('dir', models.TextField(verbose_name='Direccion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
            ],
            options={
                'verbose_name': 'Comentario Articulo',
                'verbose_name_plural': 'Comentarios Articulos',
                'ordering': ['-created'],
            },
        ),
    ]
