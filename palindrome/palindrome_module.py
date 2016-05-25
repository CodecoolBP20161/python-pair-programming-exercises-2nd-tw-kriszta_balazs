def palindrome(text):
    pal_text = text.replace(" ", "").lower()
    return pal_text == pal_text[::-1]


def main():
    print(palindrome("Indul a gorog aludni"))
    return


if __name__ == '__main__':
    main()
