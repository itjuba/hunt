# Generated by Django 3.0.2 on 2020-01-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200126_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='votes_total',
        ),
        migrations.AddField(
            model_name='product',
            name='votes_total_dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='votes_total_like',
            field=models.IntegerField(default=0),
        ),
    ]