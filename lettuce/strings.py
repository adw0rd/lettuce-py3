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

import re
import time
import unicodedata


def utf8_string(s):
    if isinstance(s, str):
        s = s.decode("utf-8")

    return s


def escape_if_necessary(what):
    what = str(what)
    if len(what) is 1:
        what = "[%s]" % what

    return what


def get_stripped_lines(string, ignore_lines_starting_with=''):
    """Split lines at newline char, then return the array of stripped lines"""
    # used e.g. to separate out all the steps in a scenario
    string = str(string)
    lines = [str(l.strip()) for l in string.splitlines()]
    if ignore_lines_starting_with:
        filter_func = lambda x: x and not x.startswith(
            ignore_lines_starting_with)
    else:
        # by using an "identity" filter function, blank lines
        # will not be included in the returned list
        filter_func = lambda x: x

    lines = list(filter(filter_func, lines))

    return lines


def split_wisely(string, sep, strip=False):
    string = str(string)
    if strip:
        string = string.strip()
    else:
        string = string.strip("\n")
    sep = str(sep)

    regex = re.compile(escape_if_necessary(sep),  re.UNICODE | re.M | re.I)

    items = [x for x in regex.split(string) if x]
    if strip:
        items = [i.strip() for i in items]
    else:
        items = [i.strip("\n") for i in items]

    return [str(i) for i in items]


def wise_startswith(string, seed):
    string = str(string).strip()
    seed = str(seed)
    regex = "^%s" % re.escape(seed)
    return bool(re.search(regex, string, re.I))


def remove_it(string, what):
    return str(re.sub(str(what), "", str(string)).strip())


def column_width(string):
    l = 0
    for c in str(string):
        if unicodedata.east_asian_width(c) in "WF":
            l += 2
        else:
            l += 1
    return l


def rfill(string, times, char=" ", append=""):
    string = str(string)
    missing = times - column_width(string)
    for x in range(missing):
        string += char

    return str(string) + str(append)


def getlen(string):
    return column_width(str(string)) + 1


def dicts_to_string(dicts, order):
    '''
    Makes dictionary ready for comparison to strings
    '''
    escape = "#{%s}" % str(time.time())

    def enline(line):
        return str(line).replace("|", escape)

    def deline(line):
        return line.replace(escape, '\\|')

    keys_and_sizes = dict([(k, getlen(k)) for k in list(dicts[0].keys())])
    for key in keys_and_sizes:
        for data in dicts:
            current_size = keys_and_sizes[key]
            value = str(data.get(key, ''))
            size = getlen(value)
            if size > current_size:
                keys_and_sizes[key] = size

    names = []
    for key in order:
        size = keys_and_sizes[key]
        name = " %s" % rfill(key, size)
        names.append(enline(name))

    table = ["|%s|" % "|".join(names)]
    for data in dicts:
        names = []
        for key in order:
            value = data.get(key, '')
            size = keys_and_sizes[key]
            names.append(enline(" %s" % rfill(value, size)))

        table.append("|%s|" % "|".join(names))

    return deline("\n".join(table) + "\n")


def parse_hashes(lines, json_format=None):
    escape = "#{%s}" % str(time.time())

    def enline(line):
        return str(line.replace("\\|", escape)).strip()

    def deline(line):
        return line.replace(escape, '|')

    def discard_comments(lines):
        return [line for line in lines if not line.startswith('#')]

    lines = discard_comments(lines)
    lines = list(map(enline, lines))

    keys = []
    hashes = []
    if lines:
        first_line = lines.pop(0)
        keys = split_wisely(first_line, "|", True)
        keys = list(map(deline, keys))

        for line in lines:
            values = split_wisely(line, "|", True)
            values = list(map(deline, values))
            hashes.append(dict(list(zip(keys, values))))

    return keys, hashes

def json_to_string(json_list, order):
    '''
    This is for aesthetic reasons, it will get the width of the largest column and
    rfill the rest with spaces
    '''
    escape = "#{%s}" % str(time.time())

    def enline(line):
        return str(line).replace("|", escape)

    def deline(line):
        return line.replace(escape, '\\|')

    nu_keys_and_sizes = list([[list(k.keys())[0], getlen(list(k.keys())[0])] for k in json_list])
    maxlen = 0
    for key_list in nu_keys_and_sizes:
        current_size = key_list[1]
        counter = 0
        temp_list = list(json_list[counter].values())[0]
        temp_maxlen = len(temp_list)
        if temp_maxlen > maxlen:
            maxlen = temp_maxlen
        for data in temp_list:
            value = str(data)
            size = getlen(value)
            if size > current_size:
                key_list[1] = size
        counter += 1
    names = []
    idx = 0
    for key in nu_keys_and_sizes:
        size = key[1]
        name = " %s" % rfill(key[0], size)
        names.append(enline(name))

    table = ["|%s|" % "|".join(names)]

    for idx in range(maxlen):
        names = []
        for data, key in zip(json_list, nu_keys_and_sizes):
            try:
                value = list(data.values())[0][idx]
            except IndexError:
                value = ''
            size = key[1]
            names.append(enline(" %s" % rfill(value, size)))
        table.append("|%s|" % "|".join(names))

    return deline("\n".join(table) + "\n")


def parse_as_json(lines):
    '''
        Parse lines into json objects
    '''
    escape = "#{%s}" % str(time.time())
    def enline(line):
        return str(line.replace("\\|", escape)).strip()

    def deline(line):
        return line.replace(escape, '|')

    def discard_comments(lines):
        return [line for line in lines if not line.startswith('#')]
    lines = discard_comments(lines)
    lines = list(map(enline, lines))
    non_unique_keys = []
    json_map = []
    if lines:
        first_line = lines.pop(0)
        non_unique_keys = split_wisely(first_line, "|", True)
        non_unique_keys = list(map(deline, non_unique_keys))
        rng_idx = len(non_unique_keys)
        json_map = list(non_unique_keys)
        for idx in range(rng_idx):
            json_map[idx] = dict([(non_unique_keys[idx], [])])
        for line in lines:
            values = split_wisely(line, "|", True)
            values = list(map(deline, values))

            for idx in range(rng_idx):
                list(json_map[idx].values())[0].append(values[idx])
    return non_unique_keys, json_map


def parse_multiline(lines):
    multilines = []
    in_multiline = False
    for line in lines:
        if line == '"""':
            in_multiline = not in_multiline
        elif in_multiline:
            if line.startswith('"'):
                line = line[1:]
            if line.endswith('"'):
                line = line[:-1]
            multilines.append(line)
    return '\n'.join(multilines)
