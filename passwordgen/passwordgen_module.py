import string
import random



lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = str(range(0,10))
chars = "[!@#$%^&*()?]"

def passwordgen():
    password = ""
    length = random.randint(8,16)
    while len(password) < length:
        rand_low = lower[random.randint(0,len(lower))]
        password = password + rand_low
        rand_up = upper[random.randint(0, len(upper))]


    return password


def main():
    solution = passwordgen()
    return solution


if __name__ == '__main__':
    main()
