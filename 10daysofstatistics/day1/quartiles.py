from statistics import median


def quartiles(n, arr):
    arr.sort()

    q2 = int(median(arr))

    mid = (n-1) // 2

    if n % 2 == 1:
        q1 = int(median(arr[:mid]))
        q3 = int(median(arr[mid+1:]))
    else:
        q1 = int(median(arr[:mid+1]))
        q3 = int(median(arr[mid+1:]))

    print(q1)
    print(q2)
    print(q3)




if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    quartiles(n,arr)
