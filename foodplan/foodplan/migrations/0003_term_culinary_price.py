# Generated by Django 4.2.5 on 2023-09-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan', '0002_culinary_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Срок')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Срок подписки',
                'verbose_name_plural': 'Срок подписки',
            },
        ),
        migrations.AddField(
            model_name='culinary',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена'),
        ),
    ]
