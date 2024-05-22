def main():

    N = int(input())

    names = []
    total = 0

    for i in range(N):
        S, C = input().split()
        names.append(S)
        total += int(C)

    names.sort()

    print(names[total % N])


if __name__ == "__main__":
    main()
