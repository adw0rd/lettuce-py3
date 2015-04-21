# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2012>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from nose.tools import assert_equals
from lettuce.core import Language, Scenario, Feature

SCENARIO = """
Сценарий: Сохранение базы курсов универитета в текстовый файл
    Пускай имеем в базе университет следующие курсы:
       | Название                | Длительность  |
       | Матан                   | 2 года        |
       | Основы программирования | 1 год         |
    Когда я сохраняю базу курсову в файл 'курсы.txt'
    Получаю в первой строке файла 'курсы.txt' строку 'Матан:2'
    И во второй строке файла 'курсы.txt' строку 'Основы программирования:1'
"""

SCENARIO_OUTLINE1 = '''
Структура сценария: Заполнение пользователей в базу
    Пускай я заполняю в поле "имя" "<имя>"
    И я заполняю в поле "возраст"  "<возраст>"
    Если я сохраняю форму
    То я вижу сообщени "Студент <имя>, возраст <возраст>, успешно занесен в базу!"

Примеры:
    | имя  | возраст |
    | Вася | 22      |
    | Петя | 30      |
'''

FEATURE = '''
Функционал: Деление чисел
  Поскольку деление сложный процесс и люди часто допускают ошибки
  Нужно дать им возможность делить на калькуляторе

  Сценарий: Целочисленное деление
    Допустим я беру калькулятор
    Тогда я делю делимое на делитель и получаю частное
    | делимое | делитель | частное |
    | 100     | 2        | 50      |
    | 28      | 7        | 4       |
    | 0       | 5        | 0       |
'''

def test_language_russian():
    'Language: RU -> Language class supports russian through code "ru"'
    lang = Language('ru')

    assert_equals(lang.code, 'ru')
    assert_equals(lang.name, 'Russian')
    assert_equals(lang.native, 'Русский')
    assert_equals(lang.feature, 'Функционал')
    assert_equals(lang.scenario, 'Сценарий')
    assert_equals(lang.examples, 'Примеры|Сценарии')
    assert_equals(lang.scenario_outline, 'Структура сценария')

def test_scenario_ru_from_string():
    'Language: RU -> Scenario.from_string'
    ru = Language('ru')
    scenario = Scenario.from_string(SCENARIO, language=ru)

    assert_equals(
        scenario.name,
        'Сохранение базы курсов универитета в текстовый файл'
    )
    assert_equals(
        scenario.steps[0].hashes,
        [
            {'Название': 'Матан', 'Длительность': '2 года'},
            {'Название': 'Основы программирования', 'Длительность': '1 год'},
        ]
    )

def test_scenario_outline1_ru_from_string():
    'Language: RU -> Scenario.from_string, with scenario outline, first case'
    ru = Language('ru')
    scenario = Scenario.from_string(SCENARIO_OUTLINE1, language=ru)

    assert_equals(
        scenario.name,
        'Заполнение пользователей в базу'
    )
    assert_equals(
        scenario.outlines,
        [
            {'имя': 'Вася', 'возраст': '22'},
            {'имя': 'Петя', 'возраст': '30'},
        ]
    )

def test_feature_ptbr_from_string():
    'Language: RU -> Feature.from_string'
    ru = Language('ru')
    feature = Feature.from_string(FEATURE, language=ru)

    assert_equals(
        feature.name,
        'Деление чисел'
    )

    assert_equals(
        feature.description,
        "Поскольку деление сложный процесс и люди часто допускают ошибки\n"
        "Нужно дать им возможность делить на калькуляторе"
    )

    (scenario, ) = feature.scenarios

    assert_equals(
        scenario.name,
        'Целочисленное деление'
    )

    assert_equals(
        scenario.steps[-1].hashes,
        [
            {'делимое': '100', 'делитель': '2', 'частное': '50'},
            {'делимое': '28', 'делитель': '7', 'частное': '4'},
            {'делимое': '0', 'делитель': '5', 'частное': '0'},
        ]
    )

