def main():
    import math

    N = int(input())
    A_C = []

    for i in range(N):
        A, C = map(int, input().split())
        A_C.append([A, C, i + 1])  # インデックスを追加

    A_C.sort(reverse=True)  # 強さで降順にソート

    S = []

    max_cost = math.inf
    for A, C, idx in A_C:
        if C <= max_cost:
            S.append(idx)
            max_cost = C

    S.sort()

    print(len(S))
    for idx in S:
        print(idx, "", end="")


if __name__ == "__main__":
    main()
