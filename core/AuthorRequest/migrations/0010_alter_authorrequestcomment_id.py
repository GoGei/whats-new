# Generated by Django 3.2.12 on 2023-09-01 21:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorRequest', '0009_alter_authorrequestcomment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorrequestcomment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        )
    ]
