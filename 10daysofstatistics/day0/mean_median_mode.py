
def mean(n, arr):
    arr_mean = sum(arr) / n

    print('%.1f' % arr_mean)

def median(n, arr):
    arr.sort()
    mid = (n - 1) // 2

    arr_median = None

    if n % 2 == 1:
        arr_median = arr[mid]
    else:
        arr_median = (arr[mid] + arr[mid + 1])/2

    print('%.1f' % arr_median)



def mode(n, arr):
    arr.sort()

    max_occur = 0
    arr_mode = None

    i = 0
    while i < n:
        count = arr.count(arr[i])
        if count > max_occur:
            max_occur = count
            arr_mode = arr[i]

        i += count

    print(arr_mode)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    mean(n, arr)
    median(n, arr)
    mode(n, arr)
