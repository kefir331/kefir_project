# Generated by Django 2.2.6 on 2019-10-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tradeorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.TextField(unique=True)),
                ('order_url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'tradeorderus',
            },
        ),
    ]
