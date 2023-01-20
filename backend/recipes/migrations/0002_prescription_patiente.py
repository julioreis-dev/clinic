# Generated by Django 3.2 on 2023-01-18 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230117_2147'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='patiente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='core.patiente'),
        ),
    ]