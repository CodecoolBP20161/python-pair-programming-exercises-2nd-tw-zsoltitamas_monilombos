import random


def listoverlap(list1, list2):
    l1 = set(list1)
    l2 = set(list2)
    l3 = l1 & l2
    l4 = list(l3)
    print(l4)
    return l4


def main():
    list1 = random.sample(range(1, 100), 5)
    print(list1)
    list2 = random.sample(range(1, 100), 5)
    print(list2)
    listoverlap(list1, list2)
    return


if __name__ == '__main__':
    main()

# >>> import random
# >>> random.sample(range(1, 100), 3)
