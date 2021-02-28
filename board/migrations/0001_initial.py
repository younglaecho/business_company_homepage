# Generated by Django 3.1.6 on 2021-02-27 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='some string', max_length=128, verbose_name='제목')),
                ('contents', models.TextField(default='some content', verbose_name='내용')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('post_type', models.CharField(max_length=32, verbose_name='게시물 종류')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_user.comuser', verbose_name='작성자')),
            ],
            options={
                'verbose_name': 'com 게시글',
                'verbose_name_plural': 'com 게시글',
                'db_table': 'com_board',
            },
        ),
    ]
