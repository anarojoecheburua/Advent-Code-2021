with open("inputs/input_data.txt") as file:
    input_data = [int(line.strip()) for line in file]

#Part 1

def count_increments(input_data):
    count = 0
    for i in range(1,len(input_data)):
        if input_data[i] - input_data[i-1] > 0:
            count +=1
    return(count)

solution = count_increments(input_data)
print(solution)

#Part 2

def count_windowincrements(input_data):
    count = 0
    for i in range(1,len(input_data) - 2):
        if input_data[i+2] - input_data[i-1] > 0:
            count +=1
    return(count)

solution = count_windowincrements(input_data)
print(solution)



