# Generated by Django 3.2.8 on 2021-10-31 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaani', '0003_rename_count_neighbourhood_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='healthno',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='policeno',
            field=models.IntegerField(null=True),
        ),
    ]
