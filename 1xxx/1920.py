######################
#
# - 문제 : 수 찾기
# - URL : https://www.acmicpc.net/problem/1920
# - 이분 탐색
#
######################

arr_num = []
target_arr_num = []


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid

        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


if __name__ == "__main__":
    N = int(input().strip())

    arr_num = list(map(int, input().strip().split(" ")))
    arr_num.sort()

    M = int(input().strip())

    target_arr_num = list(map(int, input().strip().split(" ")))

    for num in target_arr_num:

        idx = binary_search(num, arr_num)

        if idx is 0 or idx:
            print(1)
        else:
            print(0)
