
def solution(arr):
    for s in arr:
        odd = ''
        for i, c in enumerate(s):
            if i % 2:
                odd += c
            else:
                print(c, end='')

        print(' ', end='')
        print(odd)


if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split()[0])

    solution(arr)
