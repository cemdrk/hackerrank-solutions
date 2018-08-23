
# works for print , insert , remove, append, sort, pop, reverse
if __name__ == '__main__':
    arr = []
    N = int(input())

    for _ in range(N):
        command, *arguments = input().split()

        if command != 'print':
            c = 'arr.%s(%s)' % (command, ','.join(arguments))
            eval(c)
        else:
            print(arr)
