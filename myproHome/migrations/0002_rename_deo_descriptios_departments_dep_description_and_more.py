# Generated by Django 4.1.7 on 2023-05-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproHome', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='deo_descriptios',
            new_name='dep_description',
        ),
        migrations.AlterField(
            model_name='departments',
            name='dep_name',
            field=models.CharField(max_length=150),
        ),
    ]