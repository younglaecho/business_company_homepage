# Generated by Django 3.1.6 on 2021-03-18 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='notice_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.noticeboard'),
        ),
    ]
