from lettuce import world, step
from lettuce.django import mail
from lettuce.django import django_url

from nose.tools import assert_equals


@step('I visit "([^"]*)"')
def visit(step, url):
    world.browser.visit(django_url(url))


@step('I see "([^"]*)"')
def see(step, text):
    assert world.browser.is_text_present(text)


@step('an email is sent to "([^"]*?)" with subject "([^"]*)"')
def email_sent(step, to, subject):
    message = mail.queue.get(True, timeout=5)
    assert_equals(message.subject, subject)
    assert_equals(message.recipients(), [to])
