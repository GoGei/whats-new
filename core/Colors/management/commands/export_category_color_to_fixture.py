import json
import time
from pprint import pprint
from django.db import transaction
from django.core.management.base import BaseCommand
from core.Colors.models import CategoryColor
from core.Colors import constants
from core.Utils.Exporter.exporter import CrmMixinJSONExporter


class Command(BaseCommand):
    help = "Export category colors as fixture"

    def add_arguments(self, parser):
        parser.add_argument(
            "--filepath",
            type=str,
            dest="filepath",
            help="Filepath",
        )
        parser.add_argument(
            "--print_only",
            type=bool,
            dest="print_only",
            help="Only print fixture",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        data = CrmMixinJSONExporter(model=CategoryColor, export_fields=('name', 'value')).export()

        if options.get('print_only', False):
            pprint(data)
            return

        stamp = int(time.time())
        filepath = options.get('filepath', constants.CATEGORY_COLOR_DEFAULT_FIXTURE_EXPORT_PATH % stamp)
        with open(filepath, "w+") as f:
            f.write(json.dumps(data))
