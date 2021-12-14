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

def get_closers_score(opens):


def get_syntax_error_score(file):
    data = read_chunks(file)
    errors = []
    for line in data:
        result = find_first_error(line)
        if type(result) == 'str' and result in [')', ']','}','>']:
            continue
        else:
            get_closers(result)

print(get_syntax_error_score('files/day10.txt'))
