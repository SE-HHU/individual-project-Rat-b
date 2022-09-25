import random
from tkinter import W


operator = ['+','-']
vis = []
answer = []
n = int(input("你想生成的题目数量："))
while len(vis) != n:
    quantity = random.randint(2,3)
    if quantity ==2:
        a = [random.randint(0,99),random.randint(0,99)]
    elif quantity == 3:
        a = [random.randint(0,99),random.randint(0,99),random.randint(0,99)]
    s = ''
    ans = a[0]
    if len(a)==2:
        o = random.randint(0,1)
        if o == 0:
            ans+=a[1]
            s = f"{a[0]}+{a[1]}="
        else:
            ans-=a[1]
            s = f"{a[0]}-{a[1]}="
    else:
        oo = [random.randint(0,1),random.randint(0,1)]
        i = 1
        for o in oo:
            if o == '+':
                ans+=a[i]
            else:
                ans-=a[i]
            i+=1
        s = f"{a[0]}{operator[oo[0]]}{a[1]}{operator[oo[1]]}{a[2]}="
    if s not in vis and ans>= 0:
        vis.append(s)
        answer.append(ans)
f1 = open("Exercises.txt",W)
f2 = open("Answers.txt",W)
for i in range(len(vis)):
    f1.write(str(i)+'. '+vis[i]+"\n")
    f2.write(str(i)+'. '+str(answer[i])+"\n")


            
        
    
    

