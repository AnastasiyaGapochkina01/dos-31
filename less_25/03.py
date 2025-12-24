city = input("Enter your city: ")

if city == 'Rostov-on-Don' or city == 'Moscow':
    print("Location - Russia")
elif city == 'Minsk' or city == "Vitebsk":
    print('Location - "Belarus"')
else:
    print("Unknown location")

num = int(input("Enter number: "))

if num > 0 and num % 2 == 0:
    print(f"{num} is positive and even")
else:
    print("---")