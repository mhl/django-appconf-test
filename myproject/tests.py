from django.test import TestCase
from django.test.utils import override_settings


class ExampleTests(TestCase):

    @override_settings(MEDIA_ROOT='/var/tmp/')
    def test_once(self):
        response = self.client.get('/')
        self.assertContains(response, 'foo')

    @override_settings(MEDIA_ROOT='/var/tmp/')
    def test_twice(self):
        response = self.client.get('/')
        self.assertContains(response, 'foo')
