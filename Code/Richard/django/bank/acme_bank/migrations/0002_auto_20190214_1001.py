# Generated by Django 2.1.5 on 2019-02-14 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acme_bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_holder',
            new_name='account_holders',
        ),
    ]
