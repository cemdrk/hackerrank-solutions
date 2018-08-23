
def solution(arr):
    max_num = arr[0]
    sec_max = -101

    for num in arr:
        if num > max_num:
            sec_max = max_num
            max_num = num
        elif sec_max < num < max_num:
            sec_max = num

    print(sec_max)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    solution(arr)
