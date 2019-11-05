# Generated by Django 2.2.6 on 2019-11-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'country',
            },
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currency'},
        ),
    ]