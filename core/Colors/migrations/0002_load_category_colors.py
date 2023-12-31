# Generated by Django 3.2.12 on 2023-09-06 21:07

import sys

from django.db import migrations
from django.conf import settings
from core.Utils.migration import load_fixture


def load_category_colors(apps, schema):
    if settings.TEST_MODE or 'test' in sys.argv:
        return

    CategoryColor = apps.get_model('Colors', 'CategoryColor')

    qs = CategoryColor.objects.all()
    if not qs.exists():
        load_fixture(apps, 'core/Colors/fixture/category_colors_6_sep_2023.json', 'Colors.CategoryColor')
        print('[+] Load Category color fixtures')
    else:
        raise ValueError('Category colors already exists!')


class Migration(migrations.Migration):
    dependencies = [
        ('Colors', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_category_colors)
    ]
