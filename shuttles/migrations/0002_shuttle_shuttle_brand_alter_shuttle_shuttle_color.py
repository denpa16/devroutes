# Generated by Django 4.0 on 2022-06-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuttles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shuttle',
            name='shuttle_brand',
            field=models.CharField(blank=True, max_length=50, verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='shuttle',
            name='shuttle_color',
            field=models.CharField(blank=True, max_length=50, verbose_name='Цвет автомобиля'),
        ),
    ]
