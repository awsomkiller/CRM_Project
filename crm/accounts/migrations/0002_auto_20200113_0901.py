# Generated by Django 3.0 on 2020-01-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='govIdType',
            field=models.CharField(choices=[('aadhar card', 'AADHAR CARD'), ('driving license', 'DRIVING LICENSE'), ('passport', 'PASSPORT'), ('other', 'OTHER')], default='aadhar card', max_length=20),
        ),
    ]
