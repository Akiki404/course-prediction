# Generated by Django 3.1.3 on 2020-11-26 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='agreeableness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='conscientiousness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='emotions',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='extraversion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='openness',
            field=models.IntegerField(),
        ),
    ]
