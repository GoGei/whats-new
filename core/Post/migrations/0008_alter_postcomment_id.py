# Generated by Django 3.2.12 on 2023-09-02 10:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Post', '0007_alter_postcomment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        )
    ]