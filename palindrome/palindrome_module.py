def palindrome(string):
    i = 0
    boolean = False
    string = str.lower(string)
    str2 = list(string)
    str2[:] = (value for value in str2 if value != " ")
    while i < len(str2):
        if str2[i] == str2[-i-1]:
            i += 1
            if i == len(str2):
                boolean = True
                print(boolean)
        else:
            print(boolean)
            break
    return boolean


def main():
    string = input("Add a string: ")
    palindrome(string)
    return


if __name__ == '__main__':
    main()
