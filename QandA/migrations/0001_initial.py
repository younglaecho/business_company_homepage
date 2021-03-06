# Generated by Django 3.1.5 on 2021-03-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QandA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=128, verbose_name='작성자')),
                ('company', models.CharField(max_length=256, verbose_name='회사명')),
                ('email', models.CharField(max_length=256, verbose_name='이메일')),
                ('phone', models.CharField(max_length=256, verbose_name='전화번호')),
                ('fax', models.CharField(max_length=256, verbose_name='팩스번호')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '문의사항',
                'verbose_name_plural': '문의사항',
                'db_table': '문의사항',
            },
        ),
    ]
