# Generated by Django 5.0.2 on 2024-03-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_bookmodel_borrow_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='returned',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
