# Generated by Django 4.0 on 2022-06-16 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empID', models.CharField(max_length=15)),
                ('empName', models.CharField(max_length=50)),
                ('empDesgination', models.CharField(max_length=50)),
                ('empSalary', models.IntegerField()),
            ],
        ),
    ]
