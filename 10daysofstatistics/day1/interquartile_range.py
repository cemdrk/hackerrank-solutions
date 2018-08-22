
def interquartile(x, f):
    from statistics import median

    arr = []
    for num, freq in zip(x, f):
        arr += [num] * freq

    n = len(arr)

    mid = n//2

    arr.sort()
    lower = []
    upper = []

    if n % 2 == 1:
        lower = arr[:mid-1]
        upper = arr[mid+1:]
    else:
        lower = arr[:mid]
        upper = arr[mid:]

    inter_quartile = median(upper) - median(lower)

    return inter_quartile

if __name__ == '__main__':
    n = int(input())

    X = list(map(int, input().rstrip().split()))
    F = list(map(int, input().rstrip().split()))

    print('%.1f' % interquartile(X, F))
