with open("inputs/input_data.txt") as file:
    input_data = [line.strip() for line in file]

#part 1

def easy_submarine(input_data):
    horizontal = 0
    vertical = 0
    for char in input_data:
        command = char[:len(char)-2]
        position = int(char[len(char)-1:])
        if command == 'forward':
            horizontal += position
        elif command == 'up':
            vertical -= position
        else:
            vertical += position
    result = [horizontal,vertical]
    return(result)

solution = easy_submarine(input_data)
print(solution[0]*solution[1])

#part 2

def difficult_submarine(input_data):
    aim = 0
    horizontal = 0
    vertical = 0
    for char in input_data:
        command = char[:len(char)-2]
        position = int(char[len(char)-1:])
        if command == 'forward':
            horizontal += position
            vertical += (aim*position)
        elif command == 'up':
            aim -= position
        else:
            aim += position
    result = [horizontal,vertical]
    return(result)

solution = difficult_submarine(input_data)
print(solution[0]*solution[1])






