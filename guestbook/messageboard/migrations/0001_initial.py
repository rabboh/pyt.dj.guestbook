# Generated by Django 4.1.3 on 2022-12-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messageboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('postdate', models.DateField(auto_now=True)),
            ],
        ),
    ]
