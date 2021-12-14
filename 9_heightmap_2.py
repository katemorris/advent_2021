def read_map(file):
    open_file = open(file, 'r')
    lats = open_file.read().splitlines()
    open_file.close()
    return lats



def get_risk_level(file):
    map_lines = read_map(file)

    sets = []

    #map sets with starting index
    for line in map_lines:
        list_line = list(line)
        prev_char = ''
        count = 0
        set_start_index = 0
        for index, character in enumerate(list_line):
            if character == '9' and prev_char not in ['9', ''] and count > 0:
                sets.append([set_start_index, count])
                prev_char = character
                count = 0
            elif character == '9':
                prev_char = character
            elif character != '9' and prev_char == '9':
                set_start_index = index
                count += 1
                prev_char = character
            elif character != '9' and prev_char != '9':
                count += 1
                prev_char = character

    #map basins based on starting index
    #import code; code.interact(local=dict(globals(), **locals()))
    basins = []

    past_sets = {}
    for set in sets:
        index = set[0]
        count = set[1]
        minus_one = sets.get(index-1)
        plus_one = sets.get(index+1)
        import code; code.interact(local=dict(globals(), **locals()))
        if plus_one != None:
            for i in range(100)
                sets[index+1]


        else:
            import code; code.interact(local=dict(globals(), **locals()))
            print("something happened")

    product_of_basin_size = 1
    for set in basins:
        product_of_basin_size *= set
    return product_of_basin_size

print(get_risk_level('files/day9.txt'))
