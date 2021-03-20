# Generated by Django 3.1.6 on 2021-03-18 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_noticeboard_post_hit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128, verbose_name='작성자')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_date', models.DateTimeField()),
                ('notice_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.noticeboard')),
                ('reference_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.referenceboard')),
            ],
            options={
                'verbose_name': '게시판 댓글',
                'verbose_name_plural': '게시판 댓글',
                'db_table': 'com_comment',
            },
        ),
    ]
