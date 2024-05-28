# https://atcoder.jp/contests/abc032/tasks/abc032_c
def main():
    N, K = map(int, input().split())
    S = [int(input()) for _ in range(N)]

    if 0 in S:
        print(N)
        return

    result = 0
    right = 0
    product = 1

    for left in range(N):
        while right < N and product * S[right] <= K:
            product *= S[right]
            right += 1

        result = max(result, right - left)

        if left == right:
            right += 1
        else:
            product //= S[left]

    print(result)


if __name__ == "__main__":
    main()
