# Generated by Django 5.0.6 on 2024-11-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0011_alter_lesson_usd_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='usd_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена в $'),
        ),
    ]
