# Generated by Django 4.2.1 on 2023-06-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('descri', models.TextField(max_length=50)),
                ('logo', models.ImageField(upload_to='about/')),
                ('fb_link', models.URLField()),
            ],
        ),
    ]
