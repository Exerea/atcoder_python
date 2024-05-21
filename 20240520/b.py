# 354
def main():
    H = int(input())

    height = 0
    i = 0

    while height <= H:
        height += 2**i
        i += 1

    print(i)


if __name__ == "__main__":
    main()
