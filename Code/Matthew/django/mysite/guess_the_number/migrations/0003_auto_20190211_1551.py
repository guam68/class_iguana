# Generated by Django 2.1.5 on 2019-02-11 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guess_the_number', '0002_auto_20190208_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameguess',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guesses', to='guess_the_number.Game'),
        ),
    ]