with open('colors.txt') as file:
    colors = file.read()

colors = colors.split(', ')



with open('colors.txt', 'w') as file:
    for color in colors:
        file.write(color + '\n')

