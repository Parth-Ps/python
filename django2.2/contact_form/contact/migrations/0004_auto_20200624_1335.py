# Generated by Django 2.2 on 2020-06-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20200624_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AddField(
            model_name='contact',
            name='company_challenge',
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AddField(
            model_name='contact',
            name='company_website',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='contact',
            name='project_briefly',
            field=models.TextField(blank=True),
        ),
    ]
