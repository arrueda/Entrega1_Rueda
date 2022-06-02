# Generated by Django 4.0.4 on 2022-05-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teles_cur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tel_cur', models.CharField(max_length=40)),
                ('edad_tel_cur', models.IntegerField()),
                ('fechalanz_tel_cur', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teles_satel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tel_sat', models.CharField(max_length=40)),
                ('edad_tel_sat', models.IntegerField()),
                ('fechalanz_tel_sat', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teles_terr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tel_ter', models.CharField(max_length=40)),
                ('edad_tel_ter', models.IntegerField()),
                ('fechalanz_tel_ter', models.DateField()),
            ],
        ),
    ]
