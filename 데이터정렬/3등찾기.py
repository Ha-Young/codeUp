# 1420: 3등찾기

n = int(input())

students = []

for _ in range(n):
    students.append(input().split(' '))

students = sorted(students, key=lambda student: int(student[1]), reverse=True)

print(students[2][0])
