# Generated by Django 2.1 on 2018-08-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20180817_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('O', 'Online'), ('I', 'In Game'), ('F', 'Offline')], default='F', max_length=1),
        ),
    ]
