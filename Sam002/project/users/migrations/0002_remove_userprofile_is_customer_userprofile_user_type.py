# Generated by Django 4.2.6 on 2023-11-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_customer',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('customer', 'Customer'), ('agent', 'Agent')], default='customer', max_length=10),
            preserve_default=False,
        ),
    ]
