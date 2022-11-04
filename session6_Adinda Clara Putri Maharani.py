try:
    score = int(input("Score : "))
except ValueError:
    print("input must be number")
else:

    if 90 <= score <= 100:
        print("A, With Compliments")
    elif 80 <= score <= 89:
        print("B, Very Satisfy")
    elif 70 <= score <= 79:
        print("C, Satisfy")
    elif 60 <= score <=69:
        print("D, Not Satisfactory")
    elif 0 <= score <=59:
        print("E, Not Pass")
    else:
        print("the number must be 0-100")
