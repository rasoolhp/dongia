# Generated by Django 2.1.1 on 2018-09-20 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dongia_app', '0003_dongrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dongrecord',
            name='paid',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]