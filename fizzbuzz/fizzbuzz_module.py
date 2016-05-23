def fizzbuzz(number):
    to_return = ""
    if number % 3 == 0:
        if number % 5 == 0:
            to_return = "FizzBuzz"
        else:
            to_return = "Fizz"
    elif number % 5 == 0:
        to_return = "Buzz"
    else:
        to_return = number
    return to_return


def main():
    i = 1
    while i < 101:
        print(fizzbuzz(i))
        i += 1
    return

if __name__ == '__main__':
    main()
