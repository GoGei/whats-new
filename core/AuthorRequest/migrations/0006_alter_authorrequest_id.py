# Generated by Django 3.2.12 on 2023-09-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorRequest', '0005_alter_authorrequest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorrequest',
            name='id',
            field=models.CharField(auto_created=True, max_length=36, primary_key=True, serialize=False),
        ),
    ]
