const alphabet = 'abcdefghijklmnopqrstuvwxyz'
const rot_amount = 13

function init(rot_amount=13):
    rot_amount = rot_amount%26

function encrypt(text):
    s = ''
    for char in text:
        s += alphabet[(alphabet.index(char) + rot_amount)%26]
    return s

function decrypt(text):
    s = ''
    for char in text:
        s += alphabet[alphabet.index(char) - rot_amount]
    return s

