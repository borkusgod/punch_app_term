list_test = [1, 2, 3, 4]

try:
    print(list_test[4])
except IndexError:
    print("You have entered an invalid index")

