def read_coordinates(file):
    open_file = open(file, 'r')
    lines = open_file.read().splitlines()
    open_file.close()
    return lines

def make_board():
    board = {}
    for y in range(1000):
        board[y] = []
        for x in range(1000):
            board[y].append('.')
    return board

def make_int(list):
    complete = [int(i) for i in list]
    return complete

def board_count_duplicates(board):
    total = 0
    for y in board.keys():
        total += board[y].count(2)
    return total

def process_coordinates(data):
    board = make_board()

    for set in data:
        two = set.split(' -> ')
        coordinates_1 = make_int(two[0].split(','))
        coordinates_2 = make_int(two[1].split(','))
        #vertical
        if coordinates_1[0] == coordinates_2[0]:
            x = coordinates_1[0]
            for y in range(min(coordinates_1[1], coordinates_2[1]), (max(coordinates_1[1], coordinates_2[1])+1)):
                if board[y][x] == '.':
                    board[y][x] = 1
                elif board[y][x] == 1:
                    board[y][x] += 1
                else:
                    continue
        #horizontal
        elif coordinates_1[1] == coordinates_2[1]:
            y = coordinates_1[1]
            for x in range(min(coordinates_1[0], coordinates_2[0]), (max(coordinates_1[0], coordinates_2[0])+1)):
                if board[y][x] == '.':
                    board[y][x] = 1
                elif board[y][x] == 1:
                    board[y][x] += 1
                else:
                    continue
        #diagonal
        else:
            # diagonal can go both ways
            # if coordinates_1[0] > coordinates_2[0] then step up on both
            # if coordinates_1[0] < coordinates_2[0] start at bottom
            start_x = min(coordinates_1[0], coordinates_2[0])
            start_y = min(coordinates_1[1], coordinates_2[1])
            end_x = max(coordinates_1[0], coordinates_2[0])
            end_y = max(coordinates_1[1], coordinates_2[1])
            #proves 45 deg angle diagonal (always true)
            # if (end_x - start_x) == (end_y - start_y):
            #import code; code.interact(local=dict(globals(), **locals()))
            if coordinates_1[0] > coordinates_2[0] and coordinates_1[1] > coordinates_2[1]:
                for x, y in zip(reversed(range(start_x, end_x+1)),reversed(range(start_y, end_y+1))):
                    if board[y][x] == '.':
                        board[y][x] = 1
                    elif board[y][x] == 1:
                        board[y][x] += 1
                    else:
                        continue
            if coordinates_1[0] < coordinates_2[0] and coordinates_1[1] < coordinates_2[1]:
                for x, y in zip(range(start_x, end_x+1),range(start_y, end_y+1)):
                    if board[y][x] == '.':
                        board[y][x] = 1
                    elif board[y][x] == 1:
                        board[y][x] += 1
                    else:
                        continue
            if coordinates_1[0] < coordinates_2[0] and coordinates_1[1] > coordinates_2[1]:
                for x, y in zip(range(start_x, end_x+1),reversed(range(start_y, end_y+1))):
                    if board[y][x] == '.':
                        board[y][x] = 1
                    elif board[y][x] == 1:
                        board[y][x] += 1
                    else:
                        continue
            if coordinates_1[0] > coordinates_2[0] and coordinates_1[1] < coordinates_2[1]:
                for x, y in zip(reversed(range(start_x, end_x+1)),range(start_y, end_y+1)):
                    #import code; code.interact(local=dict(globals(), **locals()))
                    if board[y][x] == '.':
                        board[y][x] = 1
                    elif board[y][x] == 1:
                        board[y][x] += 1
                    else:
                        continue

    return board_count_duplicates(board)

def find_the_vents(file):
    coords = read_coordinates(file)
    len_dup_coords = process_coordinates(coords)
    print(f"There are {len_dup_coords} spots to avoid!")

find_the_vents('files/day5.txt')
