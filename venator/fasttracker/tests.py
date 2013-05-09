# coding: utf8

from django.test import TestCase
from django.core.urlresolvers import reverse as r


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('fasttracker:homepage'))

    def test_get(self):
        'GET on index must return status code 200.'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'Homepage must use template fasttracker/index.html.'
        self.assertTemplateUsed(self.resp, 'fasttracker/index.html')


class NewBugTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('fasttracker:newbug'))

    def test_get(self):
        'GET / must return status code 200.'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'NewBug must use template fasttracker/newbug.html'
        self.assertTemplateUsed(self.resp, 'fasttracker/newbug.html')
