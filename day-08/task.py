puzzle_input = []

with open("day-08/input.txt") as f:
    puzzle_input = [num.strip() for num in f.readlines()]

segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def display_clock(activated: str):
    
    res = ' ' + ('a' if 'a' in activated else '.') * 4 + ' \n'
    res += (('b' if 'b' in activated else '.') + (' ' * 4) + ('c' if 'c' in activated else '.') + '\n') * 2
    res += ' ' + ('d' if 'd' in activated else '.') * 4 + ' \n'
    res += (('e' if 'e' in activated else '.') + (' ' * 4) + ('f' if 'f' in activated else '.') + '\n') * 2
    res += ' ' + ('g' if 'g' in activated else '.') * 4 + ' \n'

    return res

# Ensuring we can display all numbers
segment_representations = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg'
]

for num, segment in enumerate(segment_representations):
    print(f'  {num}:\n{display_clock(segment)}\n\n')


# Task 1
# 1: 2 Segments
# 4: 4 Segments
# 7: 3 Segments
# 8: 7 Segments

def solve_segment(segment):
    print(f"Trying to solve {segment}")

    numbers = segment.split('|')[0].strip().split(' ')
    
    # A: Char that is in one but not in seven
    one = [seg for seg in numbers if len(seg) == 2][0]
    four = [seg for seg in numbers if len(seg) == 4][0]
    seven = [seg for seg in numbers if len(seg) == 3][0]
    char_a = [c for c in seven if c not in one][0]


    six_segments = sorted([seg for seg in numbers if len(seg) == 6])

    print(f"Six segments: {six_segments}")

    # C: All elements but one from seven are in 0, 7 and 9
    char_c = None
    for char in seven:
        if not all([char in six for six in six_segments]):
            char_c = char
            break

    # F: The other char in one that is not char_c
    char_f = [c for c in one if c != char_c][0]

    # B: In 4 and in all six_segments
    possible_char_b = [c for c in four if all([c in seg for seg in six_segments])]
    char_b = [c for c in possible_char_b if c != char_a and c != char_c and c != char_f][0]

    # D: Last unknown char in 4
    char_d = None
    for char in four:
        if char != char_b and char != char_c and char != char_f:
            char_d = char
            break

    # G: In all six segments and not yet known
    char_g = None
    for c in segments:
        if all([c in seg for seg in six_segments]):
            if c != char_a and c != char_b and c != char_d and c != char_f:
                char_g = c
                break

    # E: Last unknown char in 5-segments
    char_e = None
    for c in segments:
        if c != char_a and c != char_b and c != char_c and c != char_d and c != char_f and c != char_g:
            char_e = c

    print(f"Char a: {char_a}")
    print(f"Char b: {char_b}")
    print(f"Char c: {char_c}")
    print(f"Char d: {char_d}")
    print(f"Char e: {char_e}")
    print(f"Char f: {char_f}")
    print(f"Char g: {char_g}")

    result = ''

    for number_to_solve in segment.split('|')[1].strip().split(' '):        

        print(f"Solving number {number_to_solve}")

        for idx, possible_res in enumerate(segment_representations):  

            copy = possible_res

            rewired = copy.replace('a', '1')
            rewired = rewired.replace('b', '2')
            rewired = rewired.replace('c', '3')
            rewired = rewired.replace('d', '4')
            rewired = rewired.replace('e', '5')
            rewired = rewired.replace('f', '6')
            rewired = rewired.replace('g', '7')

            rewired = rewired.replace('1', char_a)
            rewired = rewired.replace('2', char_b)
            rewired = rewired.replace('3', char_c)
            rewired = rewired.replace('4', char_d)
            rewired = rewired.replace('5', char_e)
            rewired = rewired.replace('6', char_f)
            rewired = rewired.replace('7', char_g)

            rewired = sorted(rewired)


            # print(f"Number: {idx}:\n\tRewired: {rewired}\n\tNumber : {sorted(number_to_solve)}\n")

            if sorted(number_to_solve) == sorted(rewired):
                result += str(idx)

    print(f"Result: {result}")

    return int(result)

count = 0
for line in puzzle_input:
    back = line.split('|')[1]
    print(back)
    count += sum([1 if len(segment) in [2, 4, 3, 7] else 0 for segment in back.split(' ')])
print(count)

res = sum([solve_segment(line) for line in puzzle_input])
print(res)