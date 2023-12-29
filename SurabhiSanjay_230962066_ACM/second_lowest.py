if __name__ == '__main__':
    student =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        std1 = [name,score]
        student.append(std1)  
        
    scores = []  
    for i in student:
        if i[1] not in scores:   
            scores.append(i[1])
    scores.sort()
    second_sml = scores[1]
    names = []
    for i in student:
        if(i[1] == second_sml):
            names.append(i[0])
       
    for i in sorted(names):
        print(i)
        