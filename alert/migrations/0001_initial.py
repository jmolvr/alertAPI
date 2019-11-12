# Generated by Django 2.2.7 on 2019-11-08 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalUnifap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitute', models.FloatField()),
                ('longitude', models.FloatField()),
                ('descricao', models.CharField(max_length=140)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.LocalUnifap')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.Tipo')),
            ],
        ),
    ]
