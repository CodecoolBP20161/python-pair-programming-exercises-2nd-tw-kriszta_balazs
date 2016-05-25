def palindrome(text):
    pal_text = text.replace(" ", "").lower()
    return pal_text == pal_text[::-1]


def main():
    answer = input("Enter a sentence! ")
    print("This is " + str(palindrome(answer)))
    return palindrome(answer)


if __name__ == '__main__':
    main()
