# Generated by Django 4.2 on 2023-04-26 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_ratings_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='avgrat',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
