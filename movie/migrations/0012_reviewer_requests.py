# Generated by Django 4.0 on 2022-09-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_profreview_watchagain'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviewer_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
