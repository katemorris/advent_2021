def is_larger(set_1, set_2):
    if set_2 > set_1:
        return 1
    else:
        return 0


def larger_count(file):
    # starting counts and values
    larger_depths = 0
    # open file, do line by line
    depths_data = open(file, "r")
    depths_str = depths_data.read().splitlines()
    depths = [int(i) for i in depths_str]
    #import code; code.interact(local=dict(globals(), **locals()))
    for index_current, depth in enumerate(depths):
        if index_current == 0:
            continue
        else:
            set_1 = depths[(index_current-1):(index_current+2)]
            set_2 = depths[index_current:(index_current+3)]
            larger_depths += is_larger(sum(set_1), sum(set_2))
    depths_data.close()
    return larger_depths

count = larger_count("files/day1.txt")
print(count)
