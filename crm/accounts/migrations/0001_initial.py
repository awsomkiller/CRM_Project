# Generated by Django 3.0 on 2020-01-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userName', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('emailId', models.EmailField(max_length=120, unique=True)),
                ('fullName', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('contactNo', models.IntegerField()),
                ('panNo', models.CharField(max_length=10)),
                ('govIdType', models.CharField(max_length=10)),
                ('govId', models.IntegerField()),
                ('seniorId', models.CharField(max_length=7)),
                ('password', models.CharField(max_length=100)),
                ('superUser', models.BooleanField(default=False)),
                ('manager', models.BooleanField(default=False)),
                ('Hr', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
