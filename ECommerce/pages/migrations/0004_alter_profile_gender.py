# Generated by Django 3.2.5 on 2022-05-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_category_average_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6, null=True),
        ),
    ]
