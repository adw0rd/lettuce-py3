#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lettuce import step


def assert_in(condition, possibilities):
    assert condition in possibilities, \
        "%r 應該包含在: %r" % (
        condition, possibilities
    )

@step('輸入是(.*)')
def shu_ru(step, group):
    possibilities = [
        '什麽',
        '其他',
        '數據'
    ]
    assert_in(group, possibilities)

@step('執行(.*)時')
def zhi_xing(step, group):
    possibilities = [
        '這個',
        '這裏',
        '動作'
    ]
    assert_in(group, possibilities)

@step('得到(.*)')
def de_dao(step, group):
    possibilities = [
        '功能',
        '一樣',
        'unicode輸出!'
    ]
    assert_in(group, possibilities)
