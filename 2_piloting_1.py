def read_directions(file):
    open_file = open(file, 'r')
    directions = open_file.read().splitlines()
    open_file.close()
    return directions

def final_position(file):
    directions = read_directions(file)
    depth = 0
    position = 0
    for step in directions:
        split_step = step.split()
        direction = split_step[0]
        amount = int(split_step[1])
        if direction == 'up':
            depth -= amount
        elif direction == 'down':
            depth += amount
        elif direction == 'forward':
            position += amount
        else:
            print("oddity found")
    print(f"The depth is {depth} and horizontal position is {position}. The answer is then {position*depth}")

final_position("files/day2.txt")
