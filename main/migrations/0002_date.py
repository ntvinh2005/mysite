# Generated by Django 3.2.6 on 2021-08-15 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.note')),
            ],
        ),
    ]
