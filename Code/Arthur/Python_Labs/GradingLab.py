# we prompt by asking the user to pick a number between 0-100
score=float(input("Please enter a score number between 0 to 100 \n"))
# we compare if the score entered falls withing the range 
if score>=90 and score<=100:
   print(f"A")
#this condition is executed if the score doesn't satisfy the first condition
elif score>=80 and score<=89:
    print(f"B")
elif score>=70 and score<=79:
    print(f"C")
elif score>=60 and score<=69:
    print(f"D")
else :
    print(f"F")
 