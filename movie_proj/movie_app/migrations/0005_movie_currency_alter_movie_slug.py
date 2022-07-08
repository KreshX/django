# Generated by Django 4.0.5 on 2022-07-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('E', 'Euro'), ('D', 'Dollars'), ('R', 'Rubles')], default='R', max_length=1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
