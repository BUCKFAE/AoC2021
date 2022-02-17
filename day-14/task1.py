from operator import ne
import re

puzzle_input = []

with open("day-14/minimal_input.txt") as f:
    file_content = [line.strip() for line in f.readlines() if line.strip()]
    polymer_template = file_content[0]
    rules = file_content[1:]

print(f'Polymer template: {polymer_template}')
print('Rules:\n\t' + '\n\t'.join(rules))


for id in range(10):
    print(f'Current iteration: {id}')

    next_spaced = [f'{c}_' for c in polymer_template]
    next_spaced = ''.join(next_spaced)

    to_insert = {}

    for rule in rules:
        head, body = rule.split(' -> ')
        h1, h2 = [c for c in head]
        occurrences = [i + 1 for i in range(len(next_spaced)) if next_spaced.startswith(f'{h1}_{h2}', i)]
        to_insert[body] = to_insert.get(body, []) + occurrences


    for key, value in to_insert.items():
        for pos in value:
            next_spaced = next_spaced[:pos] + key + next_spaced[pos + 1:]


    polymer_template = next_spaced
    polymer_template = re.sub('_', '', polymer_template)


print(f'Polymer: {polymer_template}')
print(len(polymer_template))

frequency = {c : polymer_template.count(c) for c in polymer_template}
print(frequency)

res = max(frequency.values()) - min(frequency.values())

print(f'Result: {res}')
