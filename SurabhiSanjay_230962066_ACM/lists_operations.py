def printlist(lst):
    print("[",end = "")
    for i in range(len(lst)):
        if(i == len(lst)-1):
            print(lst[i], end = "]")
        else:
            print(lst[i], end = ", ")
        
if __name__ == '__main__':
    # no of commands 
    N = int(input())
    commands = []
    i = 0
    for i in range(N):
        command = input()
        commands.append(command)
    lst = []
    for i in commands :
        if "insert" in i:
            pos = int (i[7])
            num = int(i[9:11])
            lst.insert(pos, num)
        if "print" in i:
           printlist(lst) 
        if "remove" in i:
            num = int(i[7])
            if num in lst:
                lst.remove(num)
        if "append" in i :
            num = int(i[7])
            lst.append(num)
        if "sort" in i:
            lst.sort()
        if "pop" in i:
            lst.pop()
        if "reverse" in i:
            lst.sort(reverse = True)
            
            
        
        
    
    
    
                
        