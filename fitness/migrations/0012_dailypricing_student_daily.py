# Generated by Django 4.1.2 on 2024-05-10 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0011_monthlypricing_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='daily',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.dailypricing'),
        ),
    ]
