colors = ['red', 'blue', 'green', 'magenta', 'purple', 'orange']

long_colors = []

for color in colors:
    if len(color) >=5:
        long_colors.append(color)

# list comprehension
short_colors = [color for color in colors if len(color) <= 5]


nums = [1,2,3,4,5,6]

color_nums = {}
for i in range(len(colors)):
    color_nums[colors[i]] = nums[i]

# dict comprehension
color_nums = {colors[i]: nums[i] for i in range(len(colors))}

# only if you are returning a list or dict out of the list

# zip takes two lists of equal lengths and makes them a dictionary

dict(zip(colors, nums))