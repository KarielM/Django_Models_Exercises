# Generated by Django 5.0.3 on 2024-04-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Location', models.TextField()),
                ('Amount', models.FloatField()),
                ('Notes', models.TextField(null=True)),
            ],
        ),
    ]
