import datetime


def years(age):
    actual_years = datetime.datetime.now()
    return actual_years.year + 100 - age


def main():
    name = input("Enter your name:")
    user_age = int(input("Enter your age:"))
    print(years(user_age))
    return


if __name__ == '__main__':
    main()
