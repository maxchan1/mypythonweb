# Generated by Django 2.1.5 on 2019-02-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comdb', '0002_userinfo_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='发布日期')),
            ],
        ),
    ]
