def read_notes(file):
    open_file = open(file, 'r')
    lines = open_file.read().splitlines()
    puzzles = []
    for i in lines:
        outputs_one = i.split(' | ')[1]
        outputs = outputs_one.split(' ')

        inputs_one = i.split(' | ')[0]
        inputs = inputs_one.split(' ')
        puzzles.append([inputs, outputs])
    open_file.close()
    return puzzles

def sort_letters(string):
    parts = list(string)
    parts.sort()
    return parts

def break_code(input):
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    answer = { 0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    sides = {
            'top':[],
            'top_left':[],
            'top_right':[],
            'middle':[],
            'bottom':[],
            'bottom_right':[],
            'bottom_left':[]
            }
    fives = []
    sixes = []
    #sort
    for cd in input:
        len_code = len(cd)
        if len_code == 5:
            fives.append(cd)
        elif len_code == 6:
            sixes.append(cd)
        elif len_code in [2,3,4,7]:
            if len_code == 2:
                answer[1] = sort_letters(cd)
            elif len_code == 3:
                answer[7] = sort_letters(cd)

            elif len_code == 4:
                answer[4] = sort_letters(cd)
            else:
                answer[8] = sort_letters(cd)
    #side groups

    for i, letter_set in answer.items():
        if letter_set == []:
            continue
        else:
            if i == 1:
                for letter in letter_set:
                    sides['top_right'].append(letter)
                    sides['bottom_right'].append(letter)
            elif i == 4:
                letters = list(set(letter_set)-set(answer[1]))
                sides['middle'] = letters
                sides['top_left'] = letters
            elif i == 7:
                letter = list(set(letter_set)-set(answer[1]))
                sides['top'] = letter
    #sixes (must be 9,0,6)
    for value in sixes:
        sorted = sort_letters(value)
        left_over = list(set(all_letters) - set(sorted))[0]
        if left_over in sides['top_left'] and left_over in sides['middle']:
            answer[0] = sorted
            sides['middle'] = left_over
            sides['top_left'].remove(left_over)
        elif left_over not in sides['top_right'] and left_over not in sides['bottom_right']:
            answer[9] = sorted
            sides['bottom_left'] = left_over
        else:
            answer[6] = sorted
            sides['top_right'] = left_over
            sides['bottom_right'].remove(left_over)
    #fives (must be 5,2,3)
    for value in fives:
        sorted = sort_letters(value)
        left_over = list(set(all_letters) - set(sorted))
        if left_over[0] in sides['top_right'] or left_over[1] in sides['top_right']:
            answer[5] = sorted
        elif left_over[0] in sides['bottom_right'] or left_over[1] in sides['bottom_right']:
            answer[2] = sorted
        elif left_over[0] in sides['top_left'] or left_over[1] in sides['top_left']:
            answer[3] = sorted

    return answer

def get_ordered_output(output, answer):
    final_numbers = []
    for final_code in output:
        ordered = sort_letters(final_code)
        final_numbers.append([str(k) for k,v in answer.items() if v == ordered])
    final_string = final_numbers[0]+final_numbers[1]+final_numbers[2]+final_numbers[3]
    #import code; code.interact(local=dict(globals(), **locals()))
    final = int(''.join(final_string))
    return int(final)

def number_displays(file):
    puzzle_sets = read_notes(file)
    codes = []
    for puzzle in puzzle_sets:
        answer = break_code(puzzle[0])
        codes.append(get_ordered_output(puzzle[1], answer))
    return sum(codes)


print(number_displays('files/day8.txt'))
