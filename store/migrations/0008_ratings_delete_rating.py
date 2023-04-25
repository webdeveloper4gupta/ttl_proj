# Generated by Django 4.2 on 2023-04-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('rating', models.CharField(max_length=50)),
                ('prodid', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
