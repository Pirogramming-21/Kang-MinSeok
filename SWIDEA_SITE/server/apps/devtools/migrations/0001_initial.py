# Generated by Django 5.0.7 on 2024-07-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('types', models.CharField(max_length=30, verbose_name='종류')),
                ('content', models.TextField(verbose_name='설명')),
            ],
        ),
    ]
