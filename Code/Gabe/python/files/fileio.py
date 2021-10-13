
##### reading a file - no second argument necessary. Defaults to 'r' ########
# with open('example.txt') as variable_file:
#   text = variable_file.read()


#### writing in a file - second argument is a 'w' ########
# text += '\nHere is some new content'
# with open('example.txt', 'w') as cool_stuff:
#   cool_stuff.write(text)

##### append to a file - second arg is a 'a' ###########
# with open('example.txt', 'a') as file:
#   file.write('\nBluberries are actually orange')

#### old way of opening files in python ##### This way can get bugs
# file = open('example.txt')
# text = file.read()
# print(text)
# file.close()



#### Wrking with data/colors.txt #####
with open('../data/colors.txt') as file:
  colors = file.read().split(', ')

with open('../data/colors.txt', 'w') as file:
  for color in colors:
    if len(color) > 4:
      file.write(color + '\n')

# with open('../data/colors.txt', 'w') as file:
#   file.write('\n'.join(colors))

# print('\n'.join(colors))
