# Generated by Django 5.0.7 on 2024-08-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_alter_transaction_transaction_failed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='transaction_failed',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_ok',
            field=models.BooleanField(default=True),
        ),
    ]
