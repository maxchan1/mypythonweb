# Generated by Django 2.1.5 on 2019-11-07 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('comdb', '0003_auto_20191107_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='modelfile',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d80b9cc2-33a4-4cc4-9812-656d3416e80e'), editable=False),
        ),
    ]
