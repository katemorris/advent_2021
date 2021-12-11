def is_larger(input, prev_input):
    if prev_input == 0:
        return 0
    elif  input >= prev_input:
        return 1
    else:
        return 0

def larger_count(file):
    # starting counts and values
    larger_depths = 0
    prev_input = 0

    # open file, do line by line
    depths_data = open(file, "r")
    for depth in depths_data.read().splitlines():
        #import code; code.interact(local=dict(globals(), **locals()))
        larger_depths += is_larger(int(depth), prev_input)
        prev_input = int(depth)

    depths_data.close()
    return larger_depths

count = larger_count("files/day1.txt")
print(count)
