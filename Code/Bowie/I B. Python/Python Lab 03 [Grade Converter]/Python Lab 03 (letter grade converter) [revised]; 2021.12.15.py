# ---------------- #
# Python Lab 03 
# [letter grade converter--revised]
# 2021.12.15
# ---------------- #

numeric_score = float(input("Please input your score / Veuillez saisir votre note (0-100): "))

if numeric_score >= 98:
    print("A+")

elif numeric_score >= 92:
    print("A")

elif numeric_score >= 90:
    print("A-")

elif numeric_score >= 88:
    print("B+")

elif numeric_score >= 82:
    print("B")

elif numeric_score >= 80:
    print("B-")

elif numeric_score >= 78:
    print("C+")

elif numeric_score >= 72:
    print("C")

elif numeric_score >= 70:
    print("C-")

elif numeric_score >= 68:
    print("D+")

elif numeric_score >= 62:
    print("D")

elif numeric_score >= 60:
    print("D-")

elif numeric_score < 60:
    print("F")

# ---------------- #