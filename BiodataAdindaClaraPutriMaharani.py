
# This is my biodata perform by Python

#input biodata



from re import M


Name = input("enter your name           : ")
Class = input("enter your class         : ")
Major = input("enter your study program : ")
Age = int(input("enter your age            : "))
Hobbies = ["(0)", "(1)"]
Hobbies[0] = input("enter your first hobby : ")
Hobbies[1] = input("enter your second hobby : ") 
Food = bool(input("is Mie Ayam your favorite food? type Y for YES, leave blank for NO : "))
Motto = input("what's your quote : ")

#display
print("Name : ", Name)
print("Class : ", Class)
print("Major : ", Major)
print("How old are you : ", Age)
print("Hobbies : ", Hobbies)
print("Food : ", Food)
print("Motto : ", Motto)

print('nama type is : ',type(Name))
print('class type is : ',type(Class))
print('major type is : ',type(Major))
print('age type is : ',type(Age))
print('hobbies type is : ',type(Hobbies))
print('food type is : ',type(Food))
print('motto type is : ',type(Motto))