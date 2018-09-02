


if __name__ == '__main__':
    phone_book = {}
    n = int(input())

    for _ in range(n):
        name, phone_num = input().rstrip().split()
        phone_book[name] = phone_num


    while True:
        try:
            query = input()
        except:
            break

        result = phone_book.get(query)

        if result:
            print(query+'='+result)
        else:
            print('Not found')
