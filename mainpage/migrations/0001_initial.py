# Generated by Django 3.0.5 on 2020-05-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Імя блюда')),
                ('descriptions', models.TextField(verbose_name='Опис блюда')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Картинка')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Ціна')),
            ],
        ),
    ]
