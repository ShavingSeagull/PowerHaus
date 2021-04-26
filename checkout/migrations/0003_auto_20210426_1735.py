# Generated by Django 3.1 on 2021-04-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210421_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
