# Generated by Django 4.0.4 on 2022-07-06 10:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='match',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
    ]