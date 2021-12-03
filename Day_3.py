with open("inputs/input_data.txt") as file:
    input_data = [line.strip() for line in file]

#part 1

def gamma_rate_binary(input):
    addition = []
    i = 0
    solution = ''
    while i < len(input[0]):
        sum = 0 
        for j in range(len(input)-1):
            sum +=int(input[j][i])
        addition.append(sum)
        i +=1
    for num in addition:
        if len(input) - num <= num:
            solution += '1'
        else:
            solution +='0'
    return(solution)

def epsilon_rate_binary(gamma_rate):
    epsilon_rate = ''
    for char in gamma_rate:
        if char == '1':
            epsilon_rate +='0'
        else:
            epsilon_rate +='1'
    return(epsilon_rate)

def power_consumpition(gamma_rate, epsilon_rate):
    return(int(gamma_rate,2)*int(epsilon_rate,2))

#test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
#my_gamma = gamma_rate_binary(test)
#my_epsilon = epsilon_rate_binary(my_gamma)
#print(my_gamma)
#print(my_epsilon)
#print(power_consumpition(my_gamma,my_epsilon))

#my_gamma = gamma_rate_binary(input_data)
#my_epsilon = epsilon_rate_binary(my_gamma)
#print(my_gamma)
#print(my_epsilon)
#print(power_consumpition(my_gamma,my_epsilon))


#part 1

def oxigen_generator(input):
    i = 0
    solution = ''
    while i < len(input[0]) and len(input)>1:
        sum = 0
        one_bites = [] 
        zero_bites = []
        for j in range(len(input)):
            sum +=int(input[j][i])
            if int(input[j][i]) == 1:
                one_bites.append(input[j])
            else:
                zero_bites.append(input[j])
        if len(input) - sum <= sum:
            input = one_bites
        else:
            input = zero_bites
        i+=1
    return(int(input[0],2))


def co2_generator(input):
    i = 0
    solution = ''
    while i < len(input[0]) and len(input)>1:
        sum = 0
        one_bites = [] 
        zero_bites = []
        for j in range(len(input)):
            sum +=int(input[j][i])
            if int(input[j][i]) == 1:
                one_bites.append(input[j])
            else:
                zero_bites.append(input[j])
        if len(input) - sum <= sum:
            input = zero_bites
        else:
            input = one_bites
        i+=1
    return(int(input[0],2))

def solution(oxigen,co2):
    return(oxigen*co2)




test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

print(solution(co2_generator(input_data),oxigen_generator(input_data)))