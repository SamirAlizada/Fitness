# Generated by Django 4.1.2 on 2024-04-24 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0008_student_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('count', models.IntegerField()),
                ('product_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fitness.bar')),
            ],
        ),
    ]
