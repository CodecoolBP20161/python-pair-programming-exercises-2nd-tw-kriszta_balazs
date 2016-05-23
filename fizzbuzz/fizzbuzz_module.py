def fizzbuzz(number):
    to_return = ""
    if number % 3 == 0 and number % 5 == 0:
        to_return = "FizzBuzz"
    elif number % 5 == 0:
        to_return = "Buzz"
    elif number % 3 == 0:
        to_return = "Fizz"
    else:
        to_return = number
    return to_return


def main():
    for i in range(1,101):
        print(fizzbuzz(i))
    return

if __name__ == '__main__':
    main()
