
import importlib
import os
import sys

import django.core.management.base as base 

# NOTE(niklas9):
# * this is a bit hackish, but only way I found to figure out the project name
#   dynamically as for now..
project_name = os.path.dirname(os.path.abspath(sys.argv[0])).split('/')[-1]
urls = importlib.import_module('%s.urls' % project_name)


class Command(base.BaseCommand):

    help = 'Outputs all configured urls in a nice format'

    def handle(self, *args, **kwargs):
        self._print_urls(urls.urlpatterns, depth=0)

    @staticmethod
    def _print_urls(urllist, depth=0):
        for entry in urllist:
            print('  ' * depth, entry.regex.pattern)
            if hasattr(entry, 'url_patterns'):
                Command._print_urls(entry.url_patterns, depth + 1)
