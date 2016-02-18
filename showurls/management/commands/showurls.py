
import django.core.management.base as base

import testview.urls as urls

class Command(base.BaseCommand):

    help = 'Outputs all configured urls in a nice format'

    def handle(self, *args, **kwargs):
        self._print_urls(urls.urlpatterns, depth=0)

    @staticmethod
    def _print_urls(urllist, depth=0):
        for entry in urllist:
            print '  ' * depth, entry.regex.pattern
            if hasattr(entry, 'url_patterns'):
                Command._print_urls(entry.url_patterns, depth + 1)
