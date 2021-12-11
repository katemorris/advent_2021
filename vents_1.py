def read_coordinates(file):
    open_file = open(file, 'r')
    lines = open_file.read().splitlines()
    open_file.close()
    return lines

def make_int(list):
    complete = [int(i) for i in list]
    return complete

# def process_coordinates(data):
#     kept_coordinates = {'x':[], 'y':[]}
#     for set in data:
#         two = set.split(' -> ')
#         coordinates_1 = make_int(two[0].split(','))
#         coordinates_2 = make_int(two[1].split(','))
#
#         if coordinates_1[0] == coordinates_2[0]:
#             kept_coordinates['x'].append([coordinates_1, coordinates_2])
#         elif coordinates_1[1] == coordinates_2[1]:
#             kept_coordinates['y'].append([coordinates_1, coordinates_2])
#         else:
#             continue
#     return kept_coordinates

def process_coordinates(data):
    dup_coords = []
    single_coords = []
    for set in data:
        two = set.split(' -> ')
        coordinates_1 = make_int(two[0].split(','))
        coordinates_2 = make_int(two[1].split(','))

        if coordinates_1[0] == coordinates_2[0]:
            x = coordinates_1[0]
            if coordinates_1[1] >= coordinates_2[1]:
                for y in range(coordinates_2[1],(coordinates_1[1]+1)):
                    if [x,y] not in single_coords:
                        single_coords.append([x,y])
                    elif [x,y] in single_coords and [x,y] in dup_coords:
                        continue
                    elif [x,y] in single_coords and [x,y] not in dup_coords:
                        dup_coords.append([x,y])
            else:
                for y in range(coordinates_1[1],(coordinates_2[1]+1)):
                    if [x,y] not in single_coords:
                        single_coords.append([x,y])
                    elif [x,y] in single_coords and [x,y] in dup_coords:
                        continue
                    elif [x,y] in single_coords and [x,y] not in dup_coords:
                        dup_coords.append([x,y])
        elif coordinates_1[1] == coordinates_2[1]:
            y = coordinates_1[1]
            if coordinates_1[0] >= coordinates_2[0]:
                for x in range(coordinates_2[0],(coordinates_1[0]+1)):
                    if [x,y] not in single_coords:
                        single_coords.append([x,y])
                    elif [x,y] in single_coords and [x,y] in dup_coords:
                        continue
                    elif [x,y] in single_coords and [x,y] not in dup_coords:
                        dup_coords.append([x,y])
            else:
                for x in range(coordinates_1[0],(coordinates_2[0]+1)):
                    if [x,y] not in single_coords:
                        single_coords.append([x,y])
                    elif [x,y] in single_coords and [x,y] in dup_coords:
                        continue
                    elif [x,y] in single_coords and [x,y] not in dup_coords:
                        dup_coords.append([x,y])
        else:
            continue
    return len(dup_coords)

# def get_all_coord_sets(type, coord_pairs, prev_dup_set=[], prev_single_set=[]):
#
#     for pair in coord_pairs:
#
#         x
#             for i in range(pair[0][1],(pair[1][1]+1)):
#                 if [x,i] in single_coords and [x,i] in dup_coords:
#                     continue
#                 elif [x,i] in single_coords and [x,i] not in dup_coords:
#                     dup_coords.append([x,i])
#                 else:
#                     single_coords.append([x,i])
#
#     y
#             for i in range(pair[0][0],(pair[1][0]+1)):
#                 if [i,y] in single_coords and [i,y] in dup_coords:
#                     continue
#                 elif [i,y] in single_coords and [i,y] not in dup_coords:
#                     dup_coords.append([i,y])
#                 else:
#                     single_coords.append([i,y])
#     return [dup_coords, single_coords]

# def mapping_time(coordinates):
#     dup_xs = get_all_coord_sets('x',coordinates['x'])
#     all_dups = get_all_coord_sets('y',coordinates['y'],dup_xs[0], dup_xs[1])
#     return all_dups[0]

def find_the_vents(file):
    coords = read_coordinates(file)
    len_dup_coords = process_coordinates(coords)
    import code; code.interact(local=dict(globals(), **locals()))
    print(f"There are {len_dup_coords} spots to avoid!")

find_the_vents('files/day5.txt')
