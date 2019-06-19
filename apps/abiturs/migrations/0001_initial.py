# Generated by Django 2.2.2 on 2019-06-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abitur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('passport_serial', models.CharField(max_length=9)),
                ('passport_given_date', models.DateField()),
                ('passport_expiry_date', models.DateField()),
                ('passport_given_by', models.CharField(max_length=30)),
            ],
        ),
    ]
