# Generated by Django 3.2.6 on 2021-09-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210910_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]