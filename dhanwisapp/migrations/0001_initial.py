# Generated by Django 5.0.2 on 2024-03-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('phno', models.BigIntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]
