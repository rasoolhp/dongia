# Generated by Django 2.1.1 on 2018-09-20 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dongia_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('donger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donger', to='dongia_app.User')),
                ('dongia', models.ManyToManyField(to='dongia_app.User')),
            ],
        ),
    ]
