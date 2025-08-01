# Generated by Django 5.2.3 on 2025-06-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('capital', models.CharField(max_length=30)),
                ('num_provincias', models.CharField(max_length=200)),
                ('num_habitantes', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='numerotelefonico',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
