# Generated by Django 4.1.6 on 2023-03-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
                ('age', models.IntegerField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('studying_year', models.IntegerField(max_length=255)),
                ('DateofBirth', models.DateField()),
            ],
        ),
    ]
