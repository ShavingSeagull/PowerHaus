# Generated by Django 3.1 on 2021-04-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='This user likes to keep an air of mystery about them...', max_length=300),
        ),
    ]