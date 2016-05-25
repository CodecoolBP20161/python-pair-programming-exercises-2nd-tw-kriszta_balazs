def palindrome(text):
    pal_text = text.replace(" ", "")
    if pal_text == pal_text[::-1]:
        return True


def main():
    print(palindrome("indul a gorog aludni"))
    return


if __name__ == '__main__':
    main()
