# coding: utf8

from django.test import TestCase
from django.core.urlresolvers import reverse as r

from venator.fasttracker.models import Bug


class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('fasttracker:index'))

    def test_get(self):
        'GET on index must return status code 200.'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'Index must use template fasttracker/index.html.'
        self.assertTemplateUsed(self.resp, 'fasttracker/index.html')


class NewBugTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('fasttracker:newbug'))

    def test_get(self):
        'GET / must return status code 200.'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'NewBug must use template fasttracker/bug_form.html'
        self.assertTemplateUsed(self.resp, 'fasttracker/bug_form.html')


class BugDetailTest(TestCase):
    def setUp(self):
        Bug(title="Zijdsij").save()
        self.resp = self.client.get(r('fasttracker:bugdetail', args=(1,)))

    def test_get(self):
        'GET / must return status code 200.'
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        'NewBug must use template fasttracker/bug_detail.html'
        self.assertTemplateUsed(self.resp, 'fasttracker/bug_detail.html')
