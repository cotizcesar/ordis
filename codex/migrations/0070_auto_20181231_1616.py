# Generated by Django 2.1.4 on 2018-12-31 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0069_auto_20181231_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtipe',
            name='tipe',
        ),
        migrations.AddField(
            model_name='item',
            name='tipe',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='codex.ItemTipe'),
            preserve_default=False,
        ),
    ]
