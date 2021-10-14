import random #<----import random for extra challenge 1


    # Get grade value
grade = input("Enter a test score: ")#<---3.1
numgrade = int(grade)   

# Extra Challenge 2
ext_Chall = numgrade % 10

if ext_Chall > 4:
    chall2 = "+"
elif  ext_Chall == 0:
    chall2 = " "
else:
    chall2 = "-"
#3.2-----
if numgrade > 90:
    print(f"A{chall2}")
elif numgrade > 79  and numgrade < 90:
    print(f"B{chall2}")
elif numgrade > 74 and numgrade < 80:
    print(f"C{chall2}")
elif numgrade > 69 and numgrade < 75:
    print(f"D{chall2}")
elif numgrade < 70:
    print(f"F{chall2}")


