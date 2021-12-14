import time

def fish_data(file):
    open_file = open(file, 'r')
    fish = open_file.read().split(',')
    fishes_num = [int(i) for i in fish]
    open_file.close()
    return fishes_num

def move_days(fishes):
    current_fishes = []
    for fish in fishes:
        if fish == 0:
            current_fishes.append(8)
            fish = 6
            current_fishes.append(fish)
        else:
            fish -= 1
            current_fishes.append(fish)
    return current_fishes

def how_many_fishes(file, days):
    fishes = fish_data(file)
    current_fishes = fishes
    for i in range(days):
        current_fishes = move_days(current_fishes)
    return len(current_fishes)

start = time.time()
print(how_many_fishes('files/day6.txt', 80))
end = time.time()
print(f"It took {end-start} seconds")
