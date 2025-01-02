#list manipuation: mencari angka terbesar dan terkecil dalam list, lalu menghapus angka terbesar/terkecil
def list_manipulation():
    numbers = []
    for i in range(10):
        num = (int(input("add numbers: ")))
        numbers.append(num)

    print("list numbers: ")
    print("smalest number: ", min(numbers))
    print("largest number: ", max(numbers))

    numbers.remove(max(numbers))
    print("list numbers without max number: ", numbers)

    second_largest = max(numbers)
    print("second largest number: ", second_largest)

    numbers.remove(second_largest)
    print("numbers after removing second largest number: ", numbers)

#tuple basic = mengecek apakah ada nama value dalam tuple
def tuple_basic():
    fruits = ("aple", "nanas", "semangka", "pir", "pisang")
    hh = input("find fruit: ")
    if hh in fruits:
        print(f"{hh} was in tuple")
    else:
        print(f"{hh} was not in tuple")

while True:
    print("\nMenu: ")
    print("1. List Manipulation")
    print("2. Tuple Basic")
    menu = input("select the menu: ")

    if menu == "1":
        list_manipulation()
    elif menu == "2":
        tuple_basic()
    else:
        "thank you"