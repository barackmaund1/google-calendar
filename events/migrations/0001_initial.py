# Generated by Django 3.0.8 on 2020-07-22 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_day', models.IntegerField(null=True)),
                ('date_month', models.IntegerField(null=True)),
                ('date_year', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('desription', models.TextField(max_length=200)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
