#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lettuce import step


def assert_in(dado, possibilidades):
    assert dado in possibilidades, \
        "%r deveria estar nas possibilidades: %r" % (
        dado, possibilidades
    )

@step('tenho o (.*)')
def dado_que_tenho(step, grupo):
    possibilidades = [
        'algo',
        'outro',
        'dados'
    ]
    assert_in(grupo, possibilidades)

@step('faço algo com (.*)')
def faco_algo_com(step, grupo):
    possibilidades = [
        'assim',
        'aqui',
        'funcionarão'
    ]
    assert_in(grupo, possibilidades)

@step('fico feliz em ver (.*)')
def fico_feliz_em_ver(step, grupo):
    possibilidades = [
        'funcional',
        'também',
        'com unicode !'
    ]
    assert_in(grupo, possibilidades)
