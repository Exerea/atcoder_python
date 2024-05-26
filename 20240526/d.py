# 尺取り
# 全ての組み合わせからlight > rightで取り除いていく方式でいくのもいい
# def main():
#     N = int(input())

#     a = [0] * N
#     b = [0] * N
#     for i in range(N):
#         a[i], b[i] = map(int, input().split())

#     a.sort()
#     b.sort()

#     count = 0
#     for i in range(N):
#         for j in range(N):
#             if a[i] > b[j]:
#                 count += 1
#             else:
#                 break
#     print(count)


# if __name__ == "__main__":
#     main()
