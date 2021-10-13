import string

words = ["apple.", "@banana", "Kiwi  ", "can't", "keyboard!", "?what", "the\ncat"]

# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.punctuation)

purge = string.punctuation + "\n"

for i in range(len(words)):
    for char in words[i]:
        if char in purge:
            words[i] = words[i].replace(char, "")
    print(words[i])
print(words)