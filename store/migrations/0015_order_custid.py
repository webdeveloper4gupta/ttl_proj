# Generated by Django 4.2 on 2023-04-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
