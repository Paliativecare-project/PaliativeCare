# Generated by Django 3.2.9 on 2021-11-28 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0003_adminlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=255)),
            ],
        ),
    ]
