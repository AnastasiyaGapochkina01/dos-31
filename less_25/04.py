i = 1
for val in 'red', 'orange', 5, 'yellow', 'green', False, 5.8:
    print(f"iteration {i}: value = {val}")
    i += 1 # i = i + 1

sum = 0
n = 5
for i in range(1, n+1):
    print(i)
    sum += i

print(sum)

i = 0
while i < 5:
    print(i)
    i += 1

while True:
    print("---Menu---")
    print("1 - Start")
    print("2 - Rules")
    print("3 - Exit")

    choice = input("Enter menu item: ")
    if choice == "1":
        print("Let`s go")
    elif choice == "2":
        print("Rules:")
    elif choice == "3":
        print("Good bye")
        break
    else:
        print("Incorrect input")