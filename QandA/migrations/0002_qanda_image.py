# Generated by Django 3.1.5 on 2021-03-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qanda',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]