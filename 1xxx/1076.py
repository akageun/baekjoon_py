######################
#
# - 문제 : 저항
# - URL : https://www.acmicpc.net/problem/1076
#
######################


color_arr = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
input_arr = []

if __name__ == "__main__":
    for i in range(3):
        input_arr.append(input().strip())

    first_sec = int(str(color_arr.index(input_arr[0])) + str(color_arr.index(input_arr[1])))

    print(first_sec * pow(10, color_arr.index(input_arr[2])))
