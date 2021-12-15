from statistics import *

def read_chunks(file):
    open_file = open(file, 'r')
    chunks = open_file.read().splitlines()
    open_file.close()
    return chunks

def find_first_error(string):
    opens = []
    for char in list(string):
        if char in ['(', '[','{','<']:
            opens.append(char)
        else:
            if char == ')' and opens[-1] == '(':
                opens.pop(-1)
            elif char == ']' and opens[-1] == '[':
                opens.pop(-1)
            elif char == '}' and opens[-1] == '{':
                opens.pop(-1)
            elif char == '>' and opens[-1] == '<':
                opens.pop(-1)
            else:
                return char
    return opens

def get_closers_score(opens):
    reversed_list = list(reversed(opens))
    closers = []
    for char in reversed_list:
        if char == '<':
            closers.append('>')
        elif char == '(':
            closers.append(')')
        elif char == '{':
            closers.append('}')
        elif char == '[':
            closers.append(']')

    total = 0
    for char in closers:
        total *= 5
        if char == ')':
            total += 1
        elif char == ']':
            total += 2
        elif char == '}':
            total += 3
        elif char == '>':
            total += 4

    return total

def get_syntax_error_score(file):
    data = read_chunks(file)
    totals = []
    for line in data:
        result = find_first_error(line)
        if isinstance(result, str) and result in [')', ']','}','>']:
            continue
        else:
            totals.append(get_closers_score(result))
    totals.sort()
    #import code; code.interact(local=dict(globals(), **locals()))
    return median(totals)

print(get_syntax_error_score('files/day10.txt'))
