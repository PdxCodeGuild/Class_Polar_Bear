import random
# message = 'It\'s Thursday!' # String are immutable
# message = message.upper()

# print(message)

colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'orange', 'purple']

# random.shuffle(colors)

# fav_colors = colors[1:4]

# print(fav_colors)

# print('beige' in colors)

greeting = 'Hellot there'

# for x in greeting:
#   print(x)

# i = 0
# while i < len(colors):
#   if 'r' in colors[i]:
#     colors[i] = 'gray'
#   i+=1

# colors.insert(0, 'brown')
# colors.remove('green')
# some_color = colors.pop(3) # removes item, and that removed item can be stored in variable
# more_colors = ['teal', 'black', 'aquamarine']
# colors.extend(more_colors) # adds new list to end of colors

# all_colors = colors + more_colors # Does not manipulate original list

# extended_more_colors = more_colors.copy() # Will not change if original list gets changed

colors.reverse()
colors.sort(reverse=True)
colors = reversed(colors)
print(colors)