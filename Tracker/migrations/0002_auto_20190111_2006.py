# Generated by Django 2.1.4 on 2019-01-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='text1',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
        migrations.AddField(
            model_name='tracker',
            name='text2',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
        migrations.AddField(
            model_name='tracker',
            name='text3',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
