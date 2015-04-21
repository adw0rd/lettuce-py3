#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lettuce import step


def assert_in(dado, possibilidades):
    assert dado in possibilidades, \
        "%r deveria estar nas possibilidades: %r" % (
        dado, possibilidades
    )

@step('un après midi de (.*)')
def un_apres_midi(step, groupe):
    possibilites = [
        'janvier',
        'aôut',
        'octobre'
    ]
    assert_in(groupe, possibilites)

@step('je veux faire la sieste')
def je_veux_dormir(step):
	pass

@step('je peux aller (.*)')
def lieux_de_sieste(step, groupe):
    possibilites = [
        'près de la cheminé',
        'dans le transat',
        'dans le canapé'
    ]
    assert_in(groupe, possibilites)

@step('fico feliz em ver (.*)')
def fico_feliz_em_ver(step, grupo):
    possibilidades = [
        'funcional',
        'também',
        'com unicode !'
    ]
    assert_in(grupo, possibilidades)
