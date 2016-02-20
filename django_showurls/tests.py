
import django.test as test

import django_showurls.management.commands.showurls as showurls


class ShowURLsTestCase(test.TestCase):

    def test_format(self):
        m = showurls.Command._print_urls
        self.assertTrue(callable(m))
