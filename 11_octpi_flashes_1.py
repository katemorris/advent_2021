def read_octopi_map(file):
    open_file = open(file, 'r')
    lines = open_file.read()
    one_line = lines.replace('\n', '')
    open_file.close()
    return [int(x) for x in list(one_line)]

def add_one_all(octopi):
    after_one = []
    for octo in octopi:
        after_one.append(octo + 1)
    return after_one

def boom_octopi(set, count=0, used=[]):
    if all(x <= 9 for x in set):
        for index in used:
            set[index] = 0
        used.clear()
        #import code; code.interact(local=dict(globals(), **locals()))
        return (count, set)

    else:
        for index, octo in enumerate(set):
            first = int(list(str(format(index, '02d')))[0])
            second = int(list(str(format(index, '02d')))[1])

            if octo >= 10 and index not in used:
                count += 1
                set[index] = 0
                used.append(index)
                if index-1 >= 0 and index-1 <= 99 and second > 0:
                    set[index-1] += 1
                if index+1 >= 0 and index+1 <= 99 and second < 9:
                    set[index+1] += 1
                if index-10 >= 0 and index-10 <= 99 and first > 0:
                    set[index-10] += 1
                if index+10 >= 0 and index+10 <= 99 and first < 9:
                    set[index+10] += 1
                if index+11 >= 0 and index+11 <= 99 and first < 9 and second < 9:
                    set[index+11] += 1
                if index-11 >= 0 and index-11 <= 99 and first > 0 and second > 0:
                    set[index-11] += 1
                if index+9 >= 0 and index+9 <= 99 and first < 9 and second > 0:
                    set[index+9] += 1
                if index-9 >= 0 and index-9 <= 99 and first > 0 and second < 9:
                    set[index-9] += 1
            elif octo >= 10 and index in used:
                set[index] = 0
        return boom_octopi(set, count, used)

def light_em_up(file, steps):
    octopi = read_octopi_map(file)
    count = 0
    for i in range(1,steps+1):
        after_one = add_one_all(octopi)
        end_step = boom_octopi(after_one)
        count += end_step[0]
        octopi.clear()
        octopi = end_step[1]

    return count
print(light_em_up('files/day11.txt', 100))
