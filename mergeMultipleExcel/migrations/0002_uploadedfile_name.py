# Generated by Django 4.2 on 2024-06-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mergeMultipleExcel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='name',
            field=models.CharField(default='robot', max_length=20),
            preserve_default=False,
        ),
    ]
