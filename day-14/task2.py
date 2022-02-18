from audioop import add
from dataclasses import dataclass, field
from operator import ne
import re
import sys
from typing import List, Optional, Dict

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

@dataclass
class Conversion:
    initial_segment: str
    resulting_segments: List[str]
    depth: int = field(hash=False)
    char_count: Dict[str, int]


# Loading rules
rules: List[Rule] = []
for rule in rule_strings:
    head, res = rule.split(' -> ')
    h1, h2 = [c for c in head]
    rules.append(Rule(h1, h2, res))

print(f'Rules: {rules}')

conversions: List[Conversion] = [] 

def add_conversion(conversion: Conversion) -> bool:
    existing = [c for c in conversions if c == conversion]
    assert len(existing) < 2
    if len(existing) == 0:
        conversions.append(conversion)


def handle_tuple(segment, depth) -> Optional[Conversion]:
    print(f'\t\tHandling tuple: {segment}')

    segments_from_rules = segment

    for rule in rules:
        if rule.h1 == segment[0] and rule.h2 == segment[1]:
            segments_from_rules = f'{segment[0]}{rule.res}{segment[1]}'

    if segments_from_rules == segment:
        return None

    char_count = {c:segment.count(c) for c in segment}
    new_conversion = Conversion(segment, segments_from_rules, depth + 1, char_count)
    add_conversion(new_conversion)
    return new_conversion




def handle_segment(segment, depth = 0):

    # Skipping if the segment is already known
    existing = [c for c in conversions if c.initial_segment == segment and c.depth <= depth]
    assert len(existing) < 2, f'{segment}'
    if len(existing) == 1:
        print(f'Segment is already known, returning')
        return

    # Skipping if the segment length is longer than 
    if len(segment) > 2 ** 40:
        print(f'Segment to long!')
        return

    added_conversions = []
    last_end = 0

    for current_end in range(1, len(segment)):
        window = segment[last_end: current_end + 1]
        print(f'\tSubwindow: {window}')
        if len([c for c in conversions if c.initial_segment == window]) == 0:
            print(f'Found unkown window')
            last = window[:]
            print(f'Last: {last}')
            tupe_res = handle_tuple(last, depth)
            added_conversions += [tupe_res]


    cons = []

    print(f'Added Conversions: {added_conversions}')
    for added_conversion in added_conversions:
        for res in added_conversion.resulting_segments:
            handle_segment(res)
            cons += [res]
    
    new_con = Conversion(segment, cons, depth + 1, {})    
    add_conversion(new_con) 


for idx in range(len(polymer_template) - 1):

    print(f'{idx:02} / {len(polymer_template) - 1:02}: {polymer_template}')
    print(' ' * 9 + ' ' * idx +  '^')

    window_word = polymer_template[0:idx + 2]

    print(f'Current window: {window_word} ({idx} - {idx + 2})')
    handle_segment(window_word, idx)

conversions.sort(key=lambda c: c.initial_segment)
print('\n'.join([str(c) for c in conversions]))
print('---------------')
print([c for c in conversions if c.initial_segment == polymer_template][0])
