import string
import random



lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#nums = str(range(0,10))
chars = "[!@#$%^&*()?]"

def passwordgen():
    password = ""
    length = random.randint(8,17)
    while len(password) < length:
        rand_low = lower[random.randint(0,len(lower)-1)]
        password = password + rand_low
        rand_up = upper[random.randint(0, len(upper)-1)]
        password = password + rand_up
        #rand_num = nums[random.randint(0, len(nums)-1)]
        password = password + str(range(10))
        rand_chars = chars[random.randint(0, len(chars)-1)]
        password = password + rand_chars


    return password


def main():
    solution = passwordgen()
    return solution


if __name__ == '__main__':
    main()
