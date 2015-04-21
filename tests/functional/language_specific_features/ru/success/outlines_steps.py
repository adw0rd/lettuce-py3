#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lettuce import step

def assert_in(text, variants):
    assert text in variants, \
        "вариант %r не должен был тестироватся, только: %r" % (
        text, variants
    )

@step('я открываю в браузере  "([^"]*)"')
def otkrivayu_v_brauzere(step, url):
    pass

@step('я заполняю в поле "Имя" "([^"]*)"')
def zapolnyau_imya(step, name):
    names=[
        "Виталий Игоревич",
        "Марина Банраул",
    ]
    assert_in(name, names)

@step('я заполняю в поле "Email" "([^"]*)"')
def zapolnyau_email(step, email):
    emails=[
        "john@gmail.org",
        "mary@email.com",
    ]
    assert_in(email, emails)

@step('я заполняю в поле "Сообщение" "([^"]*)"')
def zapolnyau_soobchenie(step, message):
    messages=[
        "Есть интересный проект, нужно обсудить",
        "Мне нравятся ваши дизайны, хочу сайт",
    ]
    assert_in(message, messages)

@step('я нажимаю "Отправить"')
def najimayu_otparavit(step):
    pass
@step('я получаю сообщение "Спасибо за ваше сообщение"')
def poluchayu_soopschenie(step):
    pass


