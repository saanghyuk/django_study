# Generated by Django 3.1.7 on 2021-03-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='memo',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='메모'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='대기중', max_length=32, verbose_name='상태'),
        ),
    ]
