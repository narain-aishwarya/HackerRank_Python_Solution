if __name__ == '__main__':
    scores = []
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if(score not in scores):
            scores.append(score)
        students.append([name, score])
        
    scores.sort()
    score_to_show = scores[1]
    student_names = sorted([name for name, score in students if score == score_to_show])
    
    for name in student_names:
        print(name)
        
