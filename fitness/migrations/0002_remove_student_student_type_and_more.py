# Generated by Django 4.1.2 on 2024-04-13 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_type',
        ),
        migrations.AlterField(
            model_name='student',
            name='months_duration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.monthlypricing'),
        ),
    ]