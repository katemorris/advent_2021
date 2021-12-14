def read_map(file):
    open_file = open(file, 'r')
    lats = open_file.read().splitlines()
    open_file.close()
    return lats

def process_lowpoints(line, prev_line, prev2_line):
    top_line_list = list(prev2_line)
    main_line_list = list(prev_line)
    bottom_line_list = list(line) if line != prev_line else []
    max_index = len(main_line_list)-1
    risks = []
    for index, i in enumerate(main_line_list):
        i = int(i)
        up = int(top_line_list[index]) if top_line_list != [] else 9
        right = int(main_line_list[index+1]) if index < max_index else 9
        left = int(main_line_list[index-1]) if index != 0 else 9
        down = int(bottom_line_list[index]) if bottom_line_list != [] else 9
        if i < up and i < down and i < right and i < left:
            #import code; code.interact(local=dict(globals(), **locals()))
            risks.append(i)
    return risks

def get_risk_level(file):
    map_lines = read_map(file)
    total_lines = len(map_lines)
    prev_line = ''
    prev2_line = ''
    low_points = []

    for line in map_lines:
        if prev_line == '' and prev2_line == '':
            prev_line = line
        elif line == map_lines[total_lines-1]:
            for low_point in process_lowpoints(line, prev_line, prev2_line):
                low_points.append(low_point)
            prev2_line = prev_line
            prev_line = line
            for low_point in process_lowpoints(line,prev_line, prev2_line):
                low_points.append(low_point)
            #import code; code.interact(local=dict(globals(), **locals()))
        else:
            for low_point in process_lowpoints(line, prev_line, prev2_line):
                low_points.append(low_point)
            prev2_line = prev_line
            prev_line = line

    return sum([x+1 for x in low_points ])

print(get_risk_level('files/day9.txt'))
