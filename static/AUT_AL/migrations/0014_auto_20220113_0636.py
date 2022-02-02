# Generated by Django 3.2.9 on 2022-01-13 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AUT_AL', '0013_portfolio_modals'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_members',
            name='specialty',
        ),
        migrations.AddField(
            model_name='faculty_members',
            name='facebook',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='faculty_members',
            name='twitter',
            field=models.CharField(blank=True, max_length=1500),
        ),
    ]