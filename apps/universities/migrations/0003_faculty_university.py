# Generated by Django 2.2.2 on 2019-06-24 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universities.University'),
        ),
    ]