#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lettuce import step


def assert_in(condition, possibilities):
    assert condition in possibilities, \
        "%r は次のリストに入っている可能性がある: %r" % (
        condition, possibilities
    )

@step('入力値を (.*) とし')
def dado_que_tenho(step, group):
    possibilities = [
        '何か',
        'その他',
        'データ'
    ]
    assert_in(group, possibilities)

@step('処理 (.*) を使って')
def faco_algo_com(step, group):
    possibilities = [
        'これ',
        'ここ',
        '動く'
    ]
    assert_in(group, possibilities)

@step('表示は (.*) である')
def fico_feliz_em_ver(step, group):
    possibilities = [
        '機能',
        '同じ',
        'unicodeで!'
    ]
    assert_in(group, possibilities)
