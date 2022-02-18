from audioop import add
from collections import Counter
from dataclasses import dataclass, field
from operator import ne
import re
import sys
from typing import List, Optional, Dict

puzzle_input = []

with open("day-14/input.txt") as f:
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


# Loading rules and alphabet
rules: List[Rule] = []
alphabet = set()
for rule in rule_strings:
    head, res = rule.split(' -> ')
    [alphabet.add(c) for c in head + res]
    h1, h2 = [c for c in head]
    rules.append(Rule(h1, h2, res))

print(f'Rules: {rules}')
print(f'Alphabet: {alphabet}')

def create_table(base_case = True):
    table = {}
    for c1 in alphabet:
        table[c1] = {} 
        for c2 in alphabet:
            table[c1][c2] = Counter([c1, c2] if base_case else [])
    return table

table = create_table()

print(table)

for step in range(40):
    new_table = create_table(base_case=False)
    for rule in rules:
        t1 = table[rule.h1][rule.res]
        t2 = table[rule.res][rule.h2]
        n = t1 + t2 - Counter([rule.res])
        new_table[rule.h1][rule.h2] = n
    table = new_table

sum = Counter()
for idx in range(len(polymer_template) - 1):
    t = polymer_template[idx:idx+2]
    res = table[t[0]][t[1]]
    sum += res - Counter(t[1])

sum += Counter([polymer_template[-1]])

print(f'{sum=}')
l = sum.most_common()
# print(l)
print(l[0][1] - l[-1][1])


