#Rot Cipher
alphas = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
     'g': 't', 'h': 'u', 'i': 'v', 'j':'w', 'k': 'x', 'l': 'y', 
     'm': 'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r': 'e', 
     's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y': 'l',
     'z': 'm'

}

output = []
def rot13():
    user_input = (input(f'Enter your text: '))
    print(user_input)

    for letter in user_input:
        if letter in alphas:
            return alphas


    

rot13()
