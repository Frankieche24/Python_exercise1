def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 2 to 6 characters
    if not 2 <= len(s) <= 6:
        return False

    # only letters and numbers (no spaces, periods, punctuation)
    if not s.isalnum() or not s.isascii():
        return False

    # must start with at least two letters
    if not s[:2].isalpha():
        return False

    # numbers only at the end; first number cannot be 0
    for i, c in enumerate(s):
        if c.isdigit():
            if c == "0":
                return False
            return s[i:].isdigit()

    return True


if __name__ == "__main__":
    main()
