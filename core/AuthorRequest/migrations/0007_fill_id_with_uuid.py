# Generated by Django 3.2.12 on 2023-09-01 20:21
import uuid
from django.db import migrations


def fill_id_with_uuid(apps, schema_editor):
    AuthorRequest = apps.get_model('AuthorRequest', 'AuthorRequest')
    AuthorRequestComment = apps.get_model('AuthorRequest', 'AuthorRequestComment')

    for author_request in AuthorRequest.objects.all():
        old_obj_id = author_request.id

        comments = AuthorRequestComment.objects.select_related('author_request').filter(author_request=author_request)
        author_request.id = uuid.uuid4()
        author_request.save()
        comments.update(author_request=author_request)

        AuthorRequest.objects.filter(id=old_obj_id).first().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('AuthorRequest', '0006_alter_authorrequest_id'),
    ]

    operations = [
        migrations.RunPython(fill_id_with_uuid)
    ]