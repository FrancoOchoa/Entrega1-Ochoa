# Generated by Django 4.1 on 2022-09-07 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTenis', '0003_alter_integrantesclub_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProveedorIndumentaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ropa', models.CharField(max_length=50)),
                ('equipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restobarclub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutas', models.CharField(max_length=50)),
                ('bebidas', models.CharField(max_length=50)),
                ('horario', models.IntegerField()),
            ],
        ),
    ]
