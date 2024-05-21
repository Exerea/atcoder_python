def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    # N: 個数を取得
    N_number = int(data[0])

    # Sを取得
    strList = data[1 : N_number + 1]

    # 答えを出力
    ans = solve(strList, N_number)
    print(ans)


# 解答を求める関数
def solve(strList, N_number):
    ans = 0
    return ans


if __name__ == "__main__":
    main()
