# Generated by Django 2.1 on 2018-09-01 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0010_auto_20180901_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='is_replayable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quest',
            name='next_quest',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nxt_quest', to='codex.Quest'),
        ),
        migrations.AddField(
            model_name='quest',
            name='previous_quest',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prv_quest', to='codex.Quest'),
        ),
    ]