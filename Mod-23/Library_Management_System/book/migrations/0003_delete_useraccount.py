# Generated by Django 5.0.2 on 2024-03-10 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_useraccount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
