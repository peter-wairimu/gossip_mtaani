# Generated by Django 3.2.8 on 2021-10-31 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0002_auto_20211031_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='Count',
            new_name='population',
        ),
    ]
