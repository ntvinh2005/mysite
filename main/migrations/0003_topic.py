# Generated by Django 3.2.6 on 2021-08-17 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning', models.BooleanField()),
                ('working', models.BooleanField()),
                ('idea', models.BooleanField()),
                ('life', models.BooleanField()),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.note')),
            ],
        ),
    ]