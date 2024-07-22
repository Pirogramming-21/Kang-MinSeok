# Generated by Django 5.0.7 on 2024-07-17 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtools', '0001_initial'),
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devtool', to='devtools.devtool', verbose_name='개발도구'),
        ),
    ]