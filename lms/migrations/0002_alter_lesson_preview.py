# Generated by Django 5.0.6 on 2024-07-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='превью'),
        ),
    ]
