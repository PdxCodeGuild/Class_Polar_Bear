# def find_word(word, amount = 13):
#   english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#   result = ''

#   for letter in word:
#     index = english.index(letter)

#     if index + amount > len(english) - 1:
#       remain = amount - (len(english) - index)
#       result += english[remain % 26]
#     else:
#       result += english[index + amount]
#   return result

# print(find_word('cat'))

nums = [1, 2, 3, 4, 5]
for x in range(len(nums)):
  print(nums[x])