def read_notes(file):
    open_file = open(file, 'r')
    lines = open_file.read().splitlines()
    output = []
    for i in lines:
        outputs_one = i.split(' | ')[1]
        outputs = outputs_one.split(' ')
        line_lengths = []
        for seg in outputs:
            line_lengths.append(len(seg))
        output.append(line_lengths)
    open_file.close()
    return output

def number_displays(file):
    outputs = read_notes(file)
    counter = 0
    for line in outputs:
        for count in line:
            #import code; code.interact(local=dict(globals(), **locals()))
            if count in [2,4,3,7]:
                counter += 1
    return counter

print(number_displays('files/day8.txt'))
