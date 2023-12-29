if __name__ == '__main__':
    print("x=")
    x = int(input())
    print("y=")
    y = int(input())
    print("z=")
    z = int(input())
    print("n=")
    n = int(input())
def mklst(a,b,c): 
    list = [a,b,c]
    return list
def list_sum(lst):
    sum_list = 0
    i = 0
    for i in lst:
        sum_list += i
    return sum_list
i = 0 
j = 0
k = 0
final_list = []
for i in range(x):
    for j in range(y):
        for k in range(k):
            sum_req = i + j + k 
            if sum_req != n:
                final_list.append(mklst(i,j,k))
                
print("there are {} elements in the final list".format(len(final_list)))