from datetime import *




def years(age):
    this_year = date.today().year
    year = (100 - age)+this_year
    return year


def main():
    name = input("What is your name?")
    age = int(input("What is your age?"))
    solution = years(age)
    print("You are going to be")
    return solution


if __name__ == '__main__':
    main()
