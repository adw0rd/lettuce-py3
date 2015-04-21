#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lettuce import step


def assert_in(condition, possibilities):
    assert condition in possibilities, \
        "%r 应该包含在: %r" % (
        condition, possibilities
    )

@step('输入是(.*)')
def shu_ru(step, group):
    possibilities = [
        '什么',
        '其他',
        '数据'
    ]
    assert_in(group, possibilities)

@step('执行(.*)时')
def zhi_xing(step, group):
    possibilities = [
        '这个',
        '这里',
        '动作'
    ]
    assert_in(group, possibilities)

@step('得到(.*)')
def de_dao(step, group):
    possibilities = [
        '功能',
        '一样',
        'unicode输出!'
    ]
    assert_in(group, possibilities)
