# Generated by Django 4.1.2 on 2024-04-13 15:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('registration_date', models.DateField(default=django.utils.timezone.now)),
                ('monthly_fee', models.FloatField()),
                ('student_fee', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('registration_date', models.DateField(default=django.utils.timezone.now)),
                ('months_duration', models.IntegerField(choices=[], default=1)),
                ('student_type', models.CharField(choices=[], default='only_gym', max_length=50)),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.trainer')),
            ],
        ),
    ]