# Generated by Django 2.1.7 on 2019-06-05 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190604_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a temp description', max_length=2500),
            preserve_default=False,
        ),
    ]