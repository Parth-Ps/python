# Generated by Django 2.2 on 2020-03-08 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2)),
                ('label', models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1)),
                ('desciption', models.TextField()),
                ('image', models.ImageField(default='default_product.jpg', upload_to='Item_picture')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
