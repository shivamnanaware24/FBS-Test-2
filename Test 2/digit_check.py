n = int(input("Eneter three digit no: "))

first = n // 100
sec = (n // 10) % 10
third = n % 10

if(first == sec * 2 and first * 2 == third):
    print("Yes, you have done it")
else:
    print("Please try next time")