numbers = [3, 5, 6, 7, 2, 4, 6, 3, 6, 10]

for number in numbers:
    result = number * 10
    print(result)


text = "To jest opis filmu"
for x in text:
    print(x.upper())


for BUZZgame in range(1, 102):
     if BUZZgame % 3 == 0 and BUZZgame % 5 == 0:
         print("FizzBuzz")
     elif BUZZgame % 3 == 0:
         print("Fizz")
     elif BUZZgame % 5 == 0:
         print("Buzz")
     else:
        print(BUZZgame)