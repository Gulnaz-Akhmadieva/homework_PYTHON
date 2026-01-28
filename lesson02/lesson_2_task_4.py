def fizz_buzz(x):
    for i in range(1, x + 1):
        if i % 15 == 0:        # проверяем деление на 15
            print("FizzBuzz")
        elif i % 3 == 0:       # на 3
            print("Fizz")
        elif i % 5 == 0:       # на 5
            print("Buzz")
        else:                  # Иначе выводим число
            print(i)


fizz_buzz(17)
