# Generated by Django 3.0.7 on 2020-07-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200708_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='jenis_kelamin',
            field=models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], default='L', max_length=100),
        ),
    ]
