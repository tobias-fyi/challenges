# Generated by Django 2.2.2 on 2019-06-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20190629_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vibrary',
            name='image',
            field=models.ImageField(blank=True, upload_to='visual_vibes'),
        ),
    ]
