with open('hawaiian_legends_of_volcanos.txt') as file:
    text = file.read()
print(len(text))

length_of_book = len(text)
for i in text:
  if i == ',' or i == '.' or i == '“' or i == '[' or i == ']' or i == '-' or i == '\n' or i == '!' or i == '?' or i == '"' or i == '(' or i == ')' or i == '/' or i == "\\" or i == ':' or i == '#' or i == '*'or i == '”' or i == '-' or i == '‘' or i == ';' or i == '{' or i == '}' or i == '%' or i == '$' or i == '—':
    text = text.replace(i, ' ')

text = text.lower()
text = ' '.join(filter(None,text.split(' ')))
text = text.split(' ')

# Count each word and get top 10
word_dict = {}
for word in text:
  if word in word_dict:
    word_dict[word] += 1
  else:
    word_dict[word] = 1

# words = list(word_dict.items())
# words.sort(key=lambda tup: tup[1], reverse=True)
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])


# Version 2 - Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.
text_len = len(text)
pair_dict = {}
for i in range(text_len):
  if i < len(text) - 1:
    pair = f"{text[i]}  {text[i+1]}"
  if pair in pair_dict:
    pair_dict[pair] += 1
  else:
    pair_dict[pair] = 1

# pairs = list(pair_dict.items())
# pairs.sort(key=lambda tup: tup[1], reverse=True)
# for i in range(min(10, len(pairs))):  # print the top 10 pairs, or all of them, whichever is smaller
#     print(pairs[i])


# Version 3 - Let the user enter a word, then show the words which most frequently follow it.
user_word = input("Enter a word: ")
followed_dict = {}
for i in range(text_len):
  if i < len(text) - 1:
    if text[i] == user_word:
      if f"{text[i]} {text[i+1]}" in followed_dict:
        followed_dict[f"{text[i]} {text[i+1]}"] += 1
      else:
        followed_dict[f"{text[i]} {text[i+1]}"] = 1

followed = list(followed_dict.items())
followed.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(followed))):  # print the top 10 followed, or all of them, whichever is smaller
    print(followed[i])

