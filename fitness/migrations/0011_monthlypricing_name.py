# Generated by Django 4.1.2 on 2024-04-24 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0010_barsold_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlypricing',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
