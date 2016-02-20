
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

    DEFAULT_INDENTATION = '  '
    DEFAULT_INDENTATION_DEPTH = 1
    START_INDENTATION_DEPTH = 0
    PRINT_URL_FORMAT = '%s%s'
    URL_ENTRY_PROPERTY = 'url_patterns'

    help = 'Outputs all configured urls in a nice format'

    def handle(self, *args, **kwargs):
        self._print_urls(urls.urlpatterns, depth=self.START_INDENTATION_DEPTH)

    @staticmethod
    def _print_urls(urllist, depth=START_INDENTATION_DEPTH):
        for entry in urllist:
            indent_s = Command.DEFAULT_INDENTATION * depth
            print(Command.PRINT_URL_FORMAT % (indent_s, entry.regex.pattern))
            if hasattr(entry, Command.URL_ENTRY_PROPERTY):
                new_depth = depth + Command.DEFAULT_INDENTATION_DEPTH
                Command._print_urls(entry.url_patterns, depth=new_depth)
