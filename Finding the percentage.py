if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    last = list(student_marks[query_name])
    per = sum(last)/len(last)
    print("{:.2f}".format(per))
