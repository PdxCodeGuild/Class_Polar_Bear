colors = ['red', 'blue', 'green', 'magenta', 'purple', 'orange']

long_colors = []

for color in colors:
    if len(color) >= 5:
        long_colors.append(color)


short_colors = [color for color in colors if len(color) <= 5]

# print(short_colors)
# print(long_colors)


nums = [1, 2, 3, 4, 5, 6]

# color_nums = {}
# for i in range(len(colors)):
#     color_nums[colors[i]] = nums[i]

color_nums = {colors[i]: nums[i] for i in range(len(colors))}

print(color_nums)