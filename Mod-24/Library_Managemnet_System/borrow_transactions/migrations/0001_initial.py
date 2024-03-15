# Generated by Django 5.0.2 on 2024-03-12 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('balance_after_borrow', models.DecimalField(decimal_places=2, max_digits=12)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_transactions', to='accounts.useraccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]