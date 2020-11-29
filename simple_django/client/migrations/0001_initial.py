# Generated by Django 3.1.3 on 2020-11-28 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last_name')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Payments',
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('percent', models.IntegerField(verbose_name='Percent')),
                ('pay_date', models.DateTimeField(verbose_name='Date payment')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clients')),
            ],
            options={
                'verbose_name_plural': 'Payments',
                'db_table': 'payments',
            },
        ),
    ]
