# Generated by Django 3.2.7 on 2021-09-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='coord1',
            field=models.DecimalField(decimal_places=20, max_digits=45, verbose_name='coord1'),
        ),
        migrations.AlterField(
            model_name='stop',
            name='coord2',
            field=models.DecimalField(decimal_places=20, max_digits=45, verbose_name='coord2'),
        ),
    ]