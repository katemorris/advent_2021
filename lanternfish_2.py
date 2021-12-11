import time

def fish_data(file):
    open_file = open(file, 'r')
    fish = open_file.read().split(',')
    fishes_num = [int(i) for i in fish]
    open_file.close()
    return fishes_num

def how_many_fishes(file, days):
    fishes = fish_data(file)

    fish_set = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fish in fishes:
        fish_set[fish] += 1

    for i in range(days):
        zeros = fish_set[0]
        fish_set = fish_set[1:]
        #import code; code.interact(local=dict(globals(), **locals()))
        fish_set[6] += zeros
        fish_set.append(zeros)

    return sum(fish_set)

start = time.time()
print(how_many_fishes('files/day6.txt', 256))
end = time.time()
print(f"It took {end-start} seconds")
