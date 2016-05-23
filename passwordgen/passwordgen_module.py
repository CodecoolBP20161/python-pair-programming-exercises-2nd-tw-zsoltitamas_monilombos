import random
from random import shuffle


def passwordgen():
    capital_letter = random.sample(range(65, 91), random.randint(2, 5))
    lower_case = random.sample(range(97, 123), random.randint(2, 5))
    symbols = random.sample(range(33, 48), random.randint(2, 5))
    random_number = random.sample(range(0, 10), random.randint(2, 5))
    for i in range(0, len(random_number)):
        random_number[i] = str(random_number[i])
    random_list = capital_letter + lower_case + symbols
    n = 0
    mylist = random_list
    for i in random_list:
        mylist[n] = chr(i)
        n = n + 1
    mylist = mylist + random_number
    shuffle(mylist)
    password = "".join(mylist)
    print(password)
    return password


def main():
    passwordgen()
    return


if __name__ == '__main__':
    main()

""" keverés"""
# from random import shuffle
# x = [[i] for i in range(10)]
# shuffle(x)
# map(str, list_of_ints)
