# Generated by Django 5.0.2 on 2024-03-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow_transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowtransaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Borrow'), (3, 'Return')], null=True),
        ),
    ]
