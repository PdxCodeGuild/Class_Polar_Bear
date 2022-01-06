# ---------------- #
# Python Lab 11
# Rotation Cypher
# 2022.01.06
# ---------------- #
# # Rot Cipher
# Directions for initial version:
    # Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, 
    # add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

    # | Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
    # |---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
    # | English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v| w| x| y| z|
    # | ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i| j| k| l| m|
# ---------------- #
# My Notes:
    # potential ways to solve: 
    #   1) coder and decoder dictionary
    #   2) using modulo property

    # testing to locate a letter, e.g. z
    #    print(ref[25])
# ---------------- #

def rot13(string):
    ref = "abcdefghijklmnopqrstuvwxyz"
    convertedString = ""
    for letter in string: 
        myIndex = ref.index(letter)
    
        convertedString+=ref[(myIndex+13)%26]
    return convertedString

#n = input("Please input the text that you would like to encrypt / Veuillez entrer le text que vous voudriez cyphrer: ")

#print(rot13(n))

# ---------------- #
## Version 2
# Allow the user to input the amount of rotation used in the encryption. (ROTN)
# ---------------- #

def ROTN(string,p):

    ref = "abcdefghijklmnopqrstuvwxyz"
    convertedString = ""
    for letter in string: 
        if letter in ref: 
            myIndex = ref.index(letter)
            convertedString+=ref[(myIndex+p)%26]
        else:
            convertedString += letter
    return convertedString

textToEncrypt = input("Please input the text that you would like to encrypt / Veuillez entrer le text que vous voudriez cyphrer: ")
rotationNumber = int(input("Also, enter the key (rotation # for the cypher) / Veuillez entrer aussi le cle (# de rotation pour le cypher): "))

print(ROTN(textToEncrypt,rotationNumber))
# ---------------- #