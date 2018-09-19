def solution(num):
    import math
    if num < 2:
        return 'Not prime'

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return 'Not prime'

    return 'Prime'


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(solution(int(input())))
