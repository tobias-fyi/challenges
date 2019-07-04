# Generated by Django 2.2.2 on 2019-06-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('vibe_type', models.CharField(max_length=50)),
                ('link', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('notes', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'vibes',
                'ordering': ['vibe_type', 'author', 'title'],
            },
        ),
        migrations.AddField(
            model_name='story',
            name='vibe',
            field=models.ManyToManyField(to='story.Vibrary'),
        ),
    ]