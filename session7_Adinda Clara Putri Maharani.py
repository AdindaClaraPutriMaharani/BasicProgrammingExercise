import os

def menu():
    print("""
1. Calculate the area of the triangle
2. Calculate the area of the rectangle
3. Determine odd and even numbers
4. Exit
""")

#calculate the area of the triangle
def triangle():
    #input the base and the height of the triangle
    base = float(input("base : "))
    height = float(input("height : "))
    #set up the formula for the area of triangle
    the_area = 0.5 * base * height
    print("the result :", the_area)

#calculate the are of the rectangle
def rectangle():
    #input the length and the width of the rectangle\
    length = float(input("length : "))
    width = float(input("width : "))
    #set up the formula for the area of the rectangle
    the_area_rectangle = length * width
    print("the result :", the_area_rectangle)

#determine odd and even numbers
def odd_and_even():
    print("determine odd and even numbers")
    number = int(input("number : "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

while(True):
    print("menu ")
    print("1. calculate the area of the triangle")
    print("2. calculate the area of the rectangle")
    print("3. determine odd and even numbers")
    print("4. exit")
    menu = input("input the menu :")
    if (menu == "1"):
        triangle()
    if (menu == "2"):
        rectangle()
    if (menu == "3"):
        odd_and_even()
    if (menu == "4"):
        break 










