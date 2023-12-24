# Generated by Django 4.2.8 on 2023-12-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='covers')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]