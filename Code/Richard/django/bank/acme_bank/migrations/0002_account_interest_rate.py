# Generated by Django 2.1.5 on 2019-02-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme_bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='interest_rate',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]
