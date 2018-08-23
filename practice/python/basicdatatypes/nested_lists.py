
def solution(arr):
    sec_lowest=[]

    min_score = arr[0][1]
    sec_score = 101

    for s in arr:
        score = s[1]
        if score < min_score:
            sec_score = min_score
            min_score = score
        elif sec_score > score > min_score:
            sec_score = score

    for s in arr:
        score = s[1]
        if score == sec_score:
            sec_lowest.append(s[0])

    sec_lowest.sort()

    for name in sec_lowest:
        print(name)



if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    solution(students)
