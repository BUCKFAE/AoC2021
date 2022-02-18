from audioop import add
from dataclasses import dataclass
from operator import ne
import re
import sys
from typing import List

puzzle_input = []

with open("day-14/minimal_input.txt") as f:
    file_content = [line.strip() for line in f.readlines() if line.strip()]
    polymer_template = file_content[0]
    rule_strings = file_content[1:]

print(f'Polymer template: {polymer_template}')

@dataclass
class Rule:
    h1: str
    h2: str
    res: str

# Loading rules
rules: List[Rule] = []
for rule in rule_strings:
    head, res = rule.split(' -> ')
    h1, h2 = [c for c in head]
    rules.append(Rule(h1, h2, res))

print(f'Rules: {rules}')

conversions = {}

def handle_tuple(segment):
    print(f'\t\tHandling tuple: {segment}')

    segments_from_rules = []

    for rule in rules:
        if rule.h1 == segment[0] and rule.h2 == segment[1]:
            segments_from_rules.append(f'{segment[0]}{rule.res}{segment[1]}')

    # No rules apply
    if not segments_from_rules:
        segments_from_rules = [segment]

    conversions[segment] = (segments_from_rules, {c: segment.count(c) for c in segment})
    print(f'\t\tTuple from rules:\n\t\t\t' + '\n\t\t\t'.join(segments_from_rules))
    print(f'\t\tAdded conversion: {conversions[segment]}')

    return conversions[segment][0]




def handle_segment(segment, height = 0):

    # Skipping if the segment is already known
    if segment in conversions.keys():
        print(f'\tSegment is already known ({segment})')
        return

    # Skipping if the segment length is longer than 
    if len(segment) > 2 ** 40:
        print(f'Segment to long!')
        return

    added_conversions = []

    for start in range(len(segment) - 1):

        current_tuple = segment[start:start + 2]
        print(f'\tCurrent tuple: {current_tuple}')
        
        tuple_conversions = handle_tuple(current_tuple)
        added_conversions += tuple_conversions

    print(f'Added Conversions: {added_conversions}')

    char_count = {}
    for current_conversion in added_conversions:
        print(f'{current_conversion=}')
        for conversion_char in current_conversion:
            char_count[conversion_char] = char_count.get(conversion_char, 0) + current_conversion.count(conversion_char) 

    for c in segment:
        char_count[c] = char_count.get(c, 0) + segment.count(c)

    conversions[segment] = (added_conversions, char_count)

    for c in added_conversions:
        handle_segment(c)


for idx in range(len(polymer_template) - 1):

    print(f'{idx:02} / {len(polymer_template) - 1:02}: {polymer_template}')
    print(' ' * 9 + ' ' * idx +  '^')

    window_word = polymer_template[0:idx + 2]

    print(f'\tCurrent window: {window_word} ({idx} - {idx + 2})')
    handle_segment(window_word)

print(conversions)
print('---------------')
print(conversions[polymer_template])

sys.exit(1)

for idx in range(40):
    print(f'Current iteration: {idx}')

    to_insert = {}

    for id, c in enumerate(polymer_template):
        if id == len(polymer_template) - 1:
            break
        possible_rules = rule_map.get(c, {})
        rule = possible_rules.get(polymer_template[id + 1], None)
        if rule is None:
            continue
        to_insert[id + 1 + len(to_insert.keys())] = rule
        
    #print(to_insert)

    for pos, value in to_insert.items():
        polymer_template = polymer_template[:pos] + value + polymer_template[pos:]

    #print(polymer_template)

 #   print(idx)
    #assert idx != 0 or polymer_template == 'NCNBCHB', polymer_template


    if idx == 13:
        print(len(polymer_template))  

        o = {}
        for i in range(len(polymer_template) - 4):
            t = polymer_template[i:i+4]
            print(t)
            o[t] = o.get(t, 0) + 1
        print(o)

        sys.exit(1)

print(f'Polymer: {polymer_template}')
print(len(polymer_template))

frequency = {c : polymer_template.count(c) for c in polymer_template}
print(frequency)

res = max(frequency.values()) - min(frequency.values())

print(f'Result: {res}')