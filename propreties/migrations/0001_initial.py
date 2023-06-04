# Generated by Django 4.2.1 on 2023-06-04 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='places/')),
            ],
        ),
        migrations.CreateModel(
            name='Proprety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='proprety/')),
                ('price', models.IntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_prt', to='propreties.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProtBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateFrome', models.DateField(default=django.utils.timezone.now)),
                ('dateTo', models.DateField(default=django.utils.timezone.now)),
                ('geust', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2)),
                ('childrene', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_propt', to='propreties.proprety')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropretyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('opp', models.TextField(max_length=200)),
                ('createdat', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_auth', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_propt', to='propreties.proprety')),
            ],
        ),
        migrations.CreateModel(
            name='ImgProprety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfield', models.ImageField(upload_to='propretyimg/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proprety_img', to='propreties.proprety')),
            ],
        ),
    ]
