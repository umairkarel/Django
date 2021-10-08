# Generated by Django 3.1.1 on 2021-07-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
    ]