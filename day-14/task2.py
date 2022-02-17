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

def handle_unknown_tuple(segment):
    print(f'\t\tHandling tuple: {segment}')

    segment_from_rules = []

    for rule in rules:
        if rule.h1 == segment[0] and rule.h2 == segment[1]:
            segment_from_rules.append(f'{segment[0]}{rule.res}{segment[1]}')

    # No rules apply
    if not segment_from_rules:
        segment_from_rules = [segment]

    conversions[segment] = (segment_from_rules, {c: segment.count(c) for c in segment})
    print(f'\t\tTuple from rules:\n\t\t\t' + '\n\t\t\t'.join(segment_from_rules))
    print(f'\t\tAdded conversion: {conversions[segment]}')

def handle_segment(start, end):
    """
    1. Iteration: AB
    2. Iteration: ABB
    3. Iteration: ABBC
    """

    segment = polymer_template[start:end]
    print(f'Handling  segment: {segment}')

    known_segment = polymer_template[start:end -1]

    # Finding the biggest known segment
    known_segment_end = id

for idx in range(len(polymer_template) - 1):

    print(f'{idx:02} / {len(polymer_template) - 1:02}: {polymer_template}')
    print(' ' * 9 + ' ' * idx +  '^')

    # Finding the biggest window
    window_end = idx + 2
    while True:
        window_word = polymer_template[idx:window_end]
        if window_word not in conversions.keys():
            break
        else:
            window_end += 1

    print(f'\tCurrent window: {window_word} ({idx} - {window_end})')
    handle_segment(window_word)

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