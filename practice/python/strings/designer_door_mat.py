
def solution(n, m):
    pattern = ".|.";

    for i in range(1, n//2 + 1):
        print(pattern.center(m, '-'))
        pattern = '.|.' + pattern + '.|.'

    print('WELCOME'.center(m, '-'))
    pattern = pattern[3:-3]
    
    for i in range(1, n//2 + 1):
        print(pattern.center(m, '-'))
        pattern = pattern[3:-3]

if __name__ == '__main__':
    n, m = list(map(int, input().rstrip().split()))
    solution(n, m)
