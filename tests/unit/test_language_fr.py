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
Scénario: Ajout de plusieurs cursus dans la base de mon université
    Soit Une liste de cursus disponibles dans mon université
        | Nom                       | Durée    |
        | Science de l'Informatique | 5 ans    |
        | Nutrition                 | 4 ans    |
    Quand je consolide la base dans 'cursus.txt'
    Alors je vois que la 1er ligne de 'cursus.txt' contient 'Science de l'Informatique:5
    Et je vois que la 2em ligne de 'cursus.txt' contient 'Nutrition:4'
"""

OUTLINED_SCENARIO = """
Plan de Scénario: Ajouter 2 nombres
    Soit <input_1> entré dans la calculatrice
    Et <input_2> entré dans la calculatrice
    Quand je presse <bouton>
    Alors je doit avoir <output> à l'écran

    Exemples:
      | input_1 | input_2 | bouton | output |
      | 20      | 30      | add    | 50     |
      | 2       | 5       | add    | 7      |
      | 0       | 40      | add    | 40     |
"""

OUTLINED_SCENARIO2 = """
Plan de Scénario: Ajouter 2 nombres
    Soit <input_1> entré dans la calculatrice
    Et <input_2> entré dans la calculatrice
    Quand je presse <bouton>
    Alors je doit avoir <output> à l'écran

    Scénarios:
      | input_1 | input_2 | bouton | output |
      | 20      | 30      | add    | 50     |
      | 2       | 5       | add    | 7      |
      | 0       | 40      | add    | 40     |
"""
OUTLINED_SCENARIO3 = """
Plan du Scénario: Ajouter 2 nombres
    Soit <input_1> entré dans la calculatrice
    Et <input_2> entré dans la calculatrice
    Quand je presse <bouton>
    Alors je doit avoir <output> à l'écran

    Scénarios:
      | input_1 | input_2 | bouton | output |
      | 20      | 30      | add    | 50     |
      | 2       | 5       | add    | 7      |
      | 0       | 40      | add    | 40     |
"""

OUTLINED_FEATURE = """
Fonctionnalité: Faire plusieur choses en même temps
    De façon à automatiser les tests
    En tant que fainéant
    J'utilise les plans de scénario

    Plan de Scénario: Ajouter 2 nombres
        Soit <input_1> entré dans la calculatrice
        Et <input_2> entré dans la calculatrice
        Quand je presse <bouton>
        Alors je doit avoir <output> à l'écran

    Exemples:
        | input_1 | input_2 | bouton | output |
        | 20      | 30      | add    | 50     |
        | 2       | 5       | add    | 7      |
        | 0       | 40      | add    | 40     |
"""
OUTLINED_FEATURE2 = """
Fonction: Faire plusieur choses en même temps
    De façon à automatiser les tests
    En tant que fainéant
    J'utilise les plans de scénario

    Plan de Scénario: Ajouter 2 nombres
        Soit <input_1> entré dans la calculatrice
        Et <input_2> entré dans la calculatrice
        Quand je presse <bouton>
        Alors je doit avoir <output> à l'écran

    Exemples:
        | input_1 | input_2 | bouton | output |
        | 20      | 30      | add    | 50     |
        | 2       | 5       | add    | 7      |
        | 0       | 40      | add    | 40     |
"""

def test_language_french():
    'Language: FR -> Language class supports french through code "fr"'
    lang = Language('fr')

    assert_equals(lang.code, 'fr')
    assert_equals(lang.name, 'French')
    assert_equals(lang.native, 'Français')
    assert_equals(lang.feature, 'Fonctionnalité|Fonction')
    assert_equals(lang.scenario, 'Scénario')
    assert_equals(lang.examples, 'Exemples|Scénarios')
    assert_equals(lang.scenario_outline, 'Plan de Scénario|Plan du Scénario')
    assert_equals(lang.scenario_separator, '(Plan de Scénario|Plan du Scénario|Scénario)')

def test_scenario_fr_from_string():
    'Language: FR -> Scenario.from_string'
    lang = Language('fr')
    scenario = Scenario.from_string(SCENARIO, language=lang)

    assert_equals(
        scenario.name,
        'Ajout de plusieurs cursus dans la base de mon université'
    )
    assert_equals(
        scenario.steps[0].hashes,
        [
            {'Nom': "Science de l'Informatique", 'Durée': '5 ans'},
            {'Nom': 'Nutrition', 'Durée': '4 ans'},
        ]
    )

def test_scenario_outline1_fr_from_string():
    'Language: FR -> Scenario.from_string, with scenario outline, first case'
    lang = Language('fr')
    scenario = Scenario.from_string(OUTLINED_SCENARIO, language=lang)

    assert_equals(
        scenario.name,
        'Ajouter 2 nombres'
    )
    assert_equals(
        scenario.outlines,
        [
            {'input_1':'20','input_2':'30','bouton':'add','output':'50'},
            {'input_1':'2','input_2':'5','bouton':'add','output':'7'},
            {'input_1':'0','input_2':'40','bouton':'add','output':'40'},
        ]
    )

def test_scenario_outline2_fr_from_string():
    'Language: FR -> Scenario.from_string, with scenario outline, second case'
    lang = Language('fr')
    scenario = Scenario.from_string(OUTLINED_SCENARIO2, language=lang)

    assert_equals(
        scenario.name,
        'Ajouter 2 nombres'
    )
    assert_equals(
        scenario.outlines,
        [
            {'input_1':'20','input_2':'30','bouton':'add','output':'50'},
            {'input_1':'2','input_2':'5','bouton':'add','output':'7'},
            {'input_1':'0','input_2':'40','bouton':'add','output':'40'},
        ]
    )
def test_scenario_outline3_fr_from_string():
    'Language: FR -> Scenario.from_string, with scenario outline, third case'
    lang = Language('fr')
    scenario = Scenario.from_string(OUTLINED_SCENARIO2, language=lang)

    assert_equals(
        scenario.name,
        'Ajouter 2 nombres'
    )
    assert_equals(
        scenario.outlines,
        [
            {'input_1':'20','input_2':'30','bouton':'add','output':'50'},
            {'input_1':'2','input_2':'5','bouton':'add','output':'7'},
            {'input_1':'0','input_2':'40','bouton':'add','output':'40'},
        ]
    )

def test_feature_fr_from_string():
    'Language: FR -> Feature.from_string'
    lang = Language('fr')

    feature = Feature.from_string(OUTLINED_FEATURE, language=lang)

    assert_equals(
        feature.name,
        'Faire plusieur choses en même temps'
    )

    assert_equals(
        feature.description,
        "De façon à automatiser les tests\n"
        "En tant que fainéant\n"
        "J'utilise les plans de scénario"
    )

    (scenario, ) = feature.scenarios

    assert_equals(
        scenario.name,
        'Ajouter 2 nombres'
    )

    assert_equals(
        scenario.outlines,
        [
            {'input_1':'20','input_2':'30','bouton':'add','output':'50'},
            {'input_1':'2','input_2':'5','bouton':'add','output':'7'},
            {'input_1':'0','input_2':'40','bouton':'add','output':'40'},
        ]
    )
def test_feature_fr_from_string2():
    'Language: FR -> Feature.from_string, alternate name'
    lang = Language('fr')

    feature = Feature.from_string(OUTLINED_FEATURE2, language=lang)

    assert_equals(
        feature.name,
        'Faire plusieur choses en même temps'
    )

    assert_equals(
        feature.description,
        "De façon à automatiser les tests\n"
        "En tant que fainéant\n"
        "J'utilise les plans de scénario"
    )

    (scenario, ) = feature.scenarios

    assert_equals(
        scenario.name,
        'Ajouter 2 nombres'
    )

    assert_equals(
        scenario.outlines,
        [
            {'input_1':'20','input_2':'30','bouton':'add','output':'50'},
            {'input_1':'2','input_2':'5','bouton':'add','output':'7'},
            {'input_1':'0','input_2':'40','bouton':'add','output':'40'},
        ]
    )
