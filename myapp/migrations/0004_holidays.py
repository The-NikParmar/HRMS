# Generated by Django 5.0.6 on 2024-07-10 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_name', models.CharField(max_length=50)),
                ('holiday_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
