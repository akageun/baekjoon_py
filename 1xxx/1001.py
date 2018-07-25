######################
#
# - 문제 : 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
# - URL : https://www.acmicpc.net/problem/1001
#
######################


def subtraction(first_num, sec_num):
    return first_num - sec_num


if __name__ == "__main__":
    arr = input().strip().split(" ")
    print(subtraction(int(arr[0]), int(arr[1])))
