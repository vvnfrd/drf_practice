# Generated by Django 5.0.6 on 2024-11-14 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_subscription_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='pay_url',
            field=models.CharField(blank=True, null=True, verbose_name='ссылка оплаты'),
        ),
    ]
