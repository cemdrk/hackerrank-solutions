
def solution(s):
    print((lambda s: any(x.isalnum() for x in s))(s))
    print((lambda s: any(x.isalpha() for x in s))(s))
    print((lambda s: any(x.isdigit() for x in s))(s))
    print((lambda s: any(x.islower() for x in s))(s))
    print((lambda s: any(x.isupper() for x in s))(s))
    

if __name__ == '__main__':
    s = input()
    solution(s)
