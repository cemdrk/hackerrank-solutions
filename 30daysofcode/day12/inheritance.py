class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.scores = scores

    def calculate(self):
        score = sum(self.scores) // len(self.scores)
        if score >= 90:
            return 'O'
        elif score >= 80:
            return 'E'
        elif score >= 70:
            return 'A'
        elif score >= 55:
            return 'P'
        elif score >= 40:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
