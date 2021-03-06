# Generated by Django 3.1 on 2021-05-06 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.TextField(blank=True, default='This user likes to keep an air of mystery about them...', max_length=300)),
                ('location', models.CharField(blank=True, default='Earth', max_length=40)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=profiles.models.image_upload)),
                ('address_1', models.CharField(blank=True, max_length=80, null=True)),
                ('address_2', models.CharField(blank=True, max_length=80, null=True)),
                ('city', models.CharField(blank=True, max_length=40, null=True)),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
