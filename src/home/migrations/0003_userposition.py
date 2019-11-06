# Generated by Django 2.2.7 on 2019-11-06 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191104_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.DecimalField(decimal_places=4, max_digits=24)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Currency')),
            ],
            options={
                'verbose_name_plural': 'user position',
            },
        ),
    ]
