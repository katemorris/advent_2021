def read_binary(file):
    open_file = open(file, 'r')
    lines = open_file.read().splitlines()
    open_file.close()
    return lines

def count_zeros(lines):
    zeros = {'sum':0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}
    for line in lines:
        characters = list(line)
        zeros['sum'] += 1
        for index, binary in enumerate(characters):
            if binary == '0':
                zeros[index] += 1
    return zeros

def oxygen_co2_split(lines, half_sum, zeros):
    oxygen = []
    co2_list = []
    for line in lines:
        characters = list(line)
        if (characters[0] == '0' and zeros[0] > half_sum) or (characters[0] == '1' and zeros[0] < half_sum):
            oxygen.append(line)
        else:
            co2_list.append(line)
    return [oxygen, co2_list]

def get_rating(type,list):
    current_set = list
    for index in range(12):
        if index == 0:
            continue
        else:
            zeros = count_zeros(current_set)
            half_sum = float(zeros['sum'])/2

            if type == 'oxygen':
                next_set = oxygen(index, current_set, half_sum, zeros)
            elif type == 'co2':
                next_set = co2(index, current_set, half_sum, zeros)

            if len(next_set) == 1:
                import code; code.interact(local=dict(globals(), **locals()))
                return next_set[0]
            else:
                current_set = next_set
                continue

def oxygen(index, current_set, half_sum, zeros):
    this_set = []
    for line in current_set:
        character_set = list(line)
        if (zeros[index] > half_sum and character_set[index] == '0') or (zeros[index] < half_sum and character_set[index] == '1') or (zeros[index] == half_sum and character_set[index] == '1'):
            this_set.append(line)
        else:
            continue
    return this_set

def co2(index, current_set, half_sum, zeros):
    this_set = []
    for line in current_set:
        character_set = list(line)
        if (zeros[index] > half_sum and character_set[index] == '1') or (zeros[index] < half_sum and character_set[index] == '0') or (zeros[index] == half_sum and character_set[index] == '0'):
            this_set.append(line)
        else:
            continue
    return this_set


def life_support(file):
    lines = read_binary(file)
    zeros = count_zeros(lines)
    half_sum = float(zeros['sum'])/2
    first_grouping = oxygen_co2_split(lines, half_sum, zeros)

    oxygen_rating = get_rating('oxygen',first_grouping[0])
    co2_rating = get_rating('co2',first_grouping[1])
    #import code; code.interact(local=dict(globals(), **locals()))
    oxygen_decimal = int(oxygen_rating,2)
    co2_decimal = int(co2_rating,2)
    print(f"The binary of oxygen is {oxygen_rating} or {oxygen_decimal}")
    print(f"The binary of co2 is {co2_rating} or {co2_decimal}")
    print(f"The life support is {co2_decimal*oxygen_decimal}")


life_support("files/day3.txt")
