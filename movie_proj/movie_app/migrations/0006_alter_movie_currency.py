# Generated by Django 4.0.5 on 2022-07-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency_alter_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollars'), ('RUB', 'Rubles')], default='R', max_length=3),
        ),
    ]
