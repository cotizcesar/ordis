# Generated by Django 2.1.4 on 2019-01-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0076_itemability_itemabilityvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemability',
            name='image',
            field=models.ImageField(blank=True, default='codex/item/ability/default.png', upload_to='codex/item/ability/'),
        ),
    ]
