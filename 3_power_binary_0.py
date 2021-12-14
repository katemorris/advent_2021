def read_binary(file):
    zeros = {'sum':0,  0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0}

    open_file = open(file, 'r')
    for line in open_file.read().splitlines():
        characters = list(line)
        zeros['sum'] += 1
        for index, binary in enumerate(characters):
            if binary == '0':
                zeros[index] += 1

    open_file.close()
    #import code; code.interact(local=dict(globals(), **locals()))
    return zeros

def power_consumption(file):
    data = read_binary(file)
    half_sum = float(data['sum'])/2
    gamma = []
    epsilon = []
    for i in range(12):
        if data[i] > half_sum:
            gamma.append('0')
            epsilon.append('1')
        elif data[i] == half_sum:
            print("Something is even!")
        else:
            gamma.append('1')
            epsilon.append('0')
    gamma_binary_string = ''.join(gamma)
    epsilon_binary_string = ''.join(epsilon)
    gamma_decimal = int(gamma_binary_string,2)
    epsilon_decimal = int(epsilon_binary_string,2)
    print(f"The binary of gamma is {gamma_binary_string} or {gamma_decimal}")
    print(f"The binary of epsilon is {epsilon_binary_string} or {epsilon_decimal}")
    print(f"The power consumption is {epsilon_decimal*gamma_decimal}")


power_consumption("files/day3.txt")
