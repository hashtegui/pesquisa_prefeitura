# Generated by Django 4.1.7 on 2023-03-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesquisa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dt_nascimento',
            field=models.DateField(null=True),
        ),
    ]
