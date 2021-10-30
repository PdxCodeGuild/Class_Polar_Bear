import string

from django.http import HttpResponse
from django.shortcuts import render

alphabet = string.ascii_lowercase
rot_amount = 13

def encrypt(text):
    s = ''
    for char in text:
        s += alphabet[(alphabet.index(char) + rot_amount)%26]
    return s

def decrypt(text):
    s = ''
    for char in text:
        s += alphabet[alphabet.index(char) - rot_amount]
    return s

def update_rot(amount):
    rot_amount = amount%26

def index(request):
    print(request.POST)
    if request.method == "GET":
        return render(request, "lab02_redo/index.html", {})

    if request.method == "POST":
        word = request.POST["word"]
        encryption = encrypt(word)
        context= {
            "encryption": encryption,
            "word": word
        }
        return render(request, "lab02_redo/index.html", context)

