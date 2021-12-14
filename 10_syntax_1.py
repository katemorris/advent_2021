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

def get_syntax_error_score(file):
    data = read_chunks(file)
    errors = []
    for line in data:
        errors.append(find_first_error(line))

    paren = errors.count(')')
    sq = errors.count(']')
    curly = errors.count('}')
    carrot = errors.count('>')

    return ((paren*3) + (sq*57) + (curly*1197) + (carrot*25137))

print(get_syntax_error_score('files/day10.txt'))
