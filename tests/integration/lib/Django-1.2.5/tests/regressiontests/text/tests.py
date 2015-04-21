# coding: utf-8
from django.test import TestCase

from django.utils.text import *
from django.utils.http import urlquote, urlquote_plus, cookie_date, http_date
from django.utils.encoding import iri_to_uri

class TextTests(TestCase):
    """
    Tests for stuff in django.utils.text and other text munging util functions.
    """

    def test_smart_split(self):

        self.assertEquals(list(smart_split(r'''This is "a person" test.''')),
            ['This', 'is', '"a person"', 'test.'])

        self.assertEquals(list(smart_split(r'''This is "a person's" test.'''))[2],
            '"a person\'s"')

        self.assertEquals(list(smart_split(r'''This is "a person\"s" test.'''))[2],
            '"a person\\"s"')

        self.assertEquals(list(smart_split('''"a 'one''')), ['"a', "'one"])

        self.assertEquals(list(smart_split(r'''all friends' tests'''))[1],
            "friends'")

        self.assertEquals(list(smart_split('url search_page words="something else"')),
            ['url', 'search_page', 'words="something else"'])

        self.assertEquals(list(smart_split("url search_page words='something else'")),
            ['url', 'search_page', "words='something else'"])

        self.assertEquals(list(smart_split('url search_page words "something else"')),
            ['url', 'search_page', 'words', '"something else"'])

        self.assertEquals(list(smart_split('url search_page words-"something else"')),
            ['url', 'search_page', 'words-"something else"'])

        self.assertEquals(list(smart_split('url search_page words=hello')),
            ['url', 'search_page', 'words=hello'])

        self.assertEquals(list(smart_split('url search_page words="something else')),
            ['url', 'search_page', 'words="something', 'else'])

        self.assertEquals(list(smart_split("cut:','|cut:' '")),
            ["cut:','|cut:' '"])

    def test_urlquote(self):

        self.assertEquals(urlquote('Paris & Orl\xe9ans'),
            'Paris%20%26%20Orl%C3%A9ans')
        self.assertEquals(urlquote('Paris & Orl\xe9ans', safe="&"),
            'Paris%20&%20Orl%C3%A9ans')
        self.assertEquals(urlquote_plus('Paris & Orl\xe9ans'),
            'Paris+%26+Orl%C3%A9ans')
        self.assertEquals(urlquote_plus('Paris & Orl\xe9ans', safe="&"),
            'Paris+&+Orl%C3%A9ans')

    def test_cookie_date(self):
        t = 1167616461.0
        self.assertEquals(cookie_date(t), 'Mon, 01-Jan-2007 01:54:21 GMT')

    def test_http_date(self):
        t = 1167616461.0
        self.assertEquals(http_date(t), 'Mon, 01 Jan 2007 01:54:21 GMT')

    def test_iri_to_uri(self):
        self.assertEquals(iri_to_uri('red%09ros\xe9#red'),
            'red%09ros%C3%A9#red')

        self.assertEquals(iri_to_uri('/blog/for/J\xfcrgen M\xfcnster/'),
            '/blog/for/J%C3%BCrgen%20M%C3%BCnster/')

        self.assertEquals(iri_to_uri('locations/%s' % urlquote_plus('Paris & Orl\xe9ans')),
            'locations/Paris+%26+Orl%C3%A9ans')

    def test_iri_to_uri_idempotent(self):
        self.assertEquals(iri_to_uri(iri_to_uri('red%09ros\xe9#red')),
            'red%09ros%C3%A9#red')
