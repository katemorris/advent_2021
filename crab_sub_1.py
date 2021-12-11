# get the median and start there
# from statistics import *

def read_crab_positions(file):
    open_file = open(file, 'r')
    crab_data = open_file.read().split(',')
    crab_pos = [int(i) for i in crab_data]
    open_file.close()
    return crab_pos

def get_fuel_cost(positions, target):
    total_fuel = 0
    for crab in positions:
        total_fuel += max(target, crab) - min(target, crab)
        #import code; code.interact(local=dict(globals(), **locals()))
    return total_fuel

def crab_formation(file):
    crab_pos = read_crab_positions(file)
    # std_dev = int(stdev(crab_pos))

    # #median
    # med=int(median(crab_pos))
    # median_cost = get_fuel_cost(crab_pos,med)
    # #mean
    # avg=int(mean(crab_pos))
    # mean_cost = get_fuel_cost(crab_pos,avg)
    # if median_cost <= mean_cost:
    #     test = med
    #     test_cost = median_cost
    # else:
    #     test = avg
    #     test_cost = mean_cost

    test_cost = get_fuel_cost(crab_pos,0)
    for i in range(min(crab_pos), max(crab_pos)):
        current_cost = get_fuel_cost(crab_pos,i)
        if current_cost < test_cost:
            test_cost = current_cost
        else:
            continue
    return test_cost

print(crab_formation('files/day7.txt'))
