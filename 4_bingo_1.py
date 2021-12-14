def read_game_data(file):
    open_file = open(file, 'r')
    lines = open_file.read().splitlines()
    bingo_numbers_string = lines[0]
    all_cards = lines[1:]
    open_file.close()
    return [bingo_numbers_string,all_cards]

def break_card_sets(card_data):
    count = 0
    cards = []
    sets = []
    for index, data_line in enumerate(card_data):
        set = []
        if data_line == '':
            count += 1
            if len(sets) == 5:
                cards.append(sets)
                sets = []
            continue
        elif index % 6 > 0 and data_line != '':
            set.append(data_line)
        sets.append(set)
    return cards

def split_twos(string):
    values = []
    n = 3
    for index in range(0, len(string), n):
        values.append(string[index : index + n-1].strip())
    return values

def all_card_nums(card):
    all_values = []
    for row in card:
        row = split_twos(row[0])
        for value in row:
            all_values.append(value)
    return all_values

def card_rows(card, bingo_numbers):
    bingo_num_index = len(bingo_numbers)
    if type(card) is dict:
        new_card = []
        for i in range(5):
            new_card.append(card[i])
        card = new_card

    for row in card:
        # check to see if one string, if so, break it.
        if len(row) == 1:
            row = split_twos(row[0])
        # check the bingo numbers
        count = 0
        for index, num in enumerate(bingo_numbers):
            if num in row:
                count += 1
                if count == 5 and index < bingo_num_index:
                    bingo_num_index = index
            else:
                continue
    #import code; code.interact(local=dict(globals(), **locals()))
    return bingo_num_index

def change_to_columns(card):
    card_data = {0:[], 1:[], 2:[], 3:[], 4:[]}
    for row in card:
        for i, num in enumerate(split_twos(row[0])):
            card_data[i].append(num)
    return card_data

def remaining_values_sum(card_nums,check_set):
    sum = 0
    for num in card_nums:
        if num not in check_set:
            sum += int(num)
    return sum

def check_cards(card_sets, bingo_numbers):
    winner_index = len(bingo_numbers)
    winner_score = 0
    for card in card_sets:
        #check the rows
        outcome = card_rows(card, bingo_numbers)
        #check the columns
        card_columns = change_to_columns(card)
        outcome2 = card_rows(card_columns, bingo_numbers)
        #all numbers
        card_nums = all_card_nums(card)
        best_outcome = min(outcome, outcome2)
        check_set = bingo_numbers[:(best_outcome+1)]
        #import code; code.interact(local=dict(globals(), **locals()))
        if best_outcome < winner_index:
            winner_index = best_outcome
            winner_score = remaining_values_sum(card_nums,check_set)
    return (winner_score * int(bingo_numbers[winner_index]))

def best_bingo_card(file):
    game_data = read_game_data(file)
    #bingo numbers
    bingo_numbers = game_data[0].split(',')
    #card sets
    card_sets = break_card_sets(game_data[1])
    winner = check_cards(card_sets, bingo_numbers)
    print(f"Winner is {winner}")

best_bingo_card("files/day4.txt")
