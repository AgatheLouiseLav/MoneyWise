# Generated by Django 4.2.3 on 2023-08-08 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_expense_description_income_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='date_to',
        ),
    ]
