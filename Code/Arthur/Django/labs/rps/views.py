from django.http.response import HttpResponse
from django.shortcuts import render
from random import choice
import random


def rpsfunc(request, user_choice):
    vailable = ('rock','paper','scissors')
    computer_choice=random.choice(vailable)
    return render(request,'rps/index.html', {
        'user_choice':user_choice,
        'computer_choice' : computer_choice,
    })
    # if user_choice == computer_choice:
    #     return HttpResponse(f"This is a tie")
    # elif user_choice == "rock" :
    #     if computer_choice == "paper" :
    #         return HttpResponse(f"The computer wins!")
    #     else:
    #         return HttpResponse(f"you win!")
    # elif user_choice == "paper" :
    #     if computer_choice == "scissors" :
    #         return HttpResponse(f"The computer Wins!")
    #     else:
    #         return HttpResponse(f"you win")
    # elif user_choice == "scissors":
    #     if computer_choice =="rock":
    #         return HttpResponse(f"The computer wins!")
    #     else:
    #         return HttpResponse(f"You win")
    # else:
    #     return HttpResponse(f"Thank you for playing,Goodbye")
 





