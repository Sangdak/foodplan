# Generated by Django 4.2.5 on 2023-09-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='culinary',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='culinary_img', verbose_name='Изображение'),
        ),
    ]
