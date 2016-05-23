import string
import random

# char_list = string.printable
# print(char_list)
# password = ""
# length = random.randint(8,16)
# print(length)
# while len(password) < length:
#     my_random = char_list[random.randint(0,len(char_list)-1)]
#     password = password + my_random
#
# print(password)





def passwordgen():
    char_list = string.printable
    password = ""
    length = random.randint(8,16)
    while len(password) < length:
        my_random = char_list[random.randint(0,len(char_list)-1)]
        password = password + my_random
    return password


def main():
    solution = passwordgen()
    return solution


if __name__ == '__main__':
    main()
