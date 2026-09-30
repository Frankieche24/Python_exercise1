def main():
    due = 50
    accepted = (25, 10, 5)

    while due > 0:
        print(f"Amount Due: {due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue
        if coin in accepted:
            due -= coin

    print(f"Change Owed: {abs(due)}")


if __name__ == "__main__":
    main()
