import copy
def short1(i,j):
    if list2[i]>=0 and list2[i]<n[0] and list2[j]-1>=0 and list2[j]-1<n[1]:
        k=list1[list2[i]][list2[j]-1]
        #print([list2[i]],[list2[j]-1],"hello")
        if k=='A':pass
        elif list3[list2[i]][list2[j]-1]==0:
            list3[list2[i]][list2[j]-1]=list3[list2[i]-1][list2[j]-1]+1
            que.append((list2[i]*10)+(list2[j]-1))
            #print((list2[i]*10)+(list2[j]-1),"hi")
        elif (list3[list2[i]-1][list2[j]-1]+1)<list3[list2[i]][list2[j]-1]:
            list3[list2[i]][list2[j]-1]=list3[list2[i]-1][list2[j]-1]+1
            que.append((list2[i]*10)+(list2[j]-1))
            #print((list2[i]*10)+(list2[j]-1),"hi")
    if list2[i]-1>=0 and list2[i]-1<n[0] and list2[j]>=0 and list2[j]<n[1]:
        l=list1[(list2[i]-1)][list2[j]]
        if l=='A':pass
        elif list3[(list2[i]-1)][list2[j]]==0:
            list3[(list2[i]-1)][list2[j]]=list3[list2[i]-1][list2[j]-1]+1
            que.append(((list2[i]-1)*10)+(list2[j]))
        elif (list3[list2[i]-1][list2[j]-1]+1)<list3[(list2[i]-1)][list2[j]]:
            list3[(list2[i]-1)][list2[j]]=list3[list2[i]-1][list2[j]-1]+1
            que.append(((list2[i]-1)*10)+(list2[j]))
    if list2[i]-2>=0 and list2[i]-2<n[0] and list2[j]-1>=0 and list2[j]-1<n[1]:
        m=list1[list2[i]-2][list2[j]-1]
        if m=='A':pass
        elif list3[list2[i]-2][list2[j]-1]==0:
            list3[list2[i]-2][list2[j]-1]=list3[list2[i]-1][list2[j]-1]+1
            que.append(((list2[i]-2)*10)+(list2[j]-1))
        elif (list3[list2[i]-1][list2[j]-1]+1)<list3[list2[i]-2][list2[j]-1]:
            list3[list2[i]-2][list2[j]-1]=list3[list2[i]-1][list2[j]-1]+1
            que.append(((list2[i]-2)*10)+(list2[j]-1))
    if list2[i]-1>=0 and list2[i]-1<n[0] and list2[j]-2>=0 and list2[j]-2<n[1]:
        n_1=list1[list2[i]-1][list2[j]-2]
        #print([list2[i]-1],[list2[j]-2],"hi")
        if n_1=='A':pass
        elif list3[list2[i]-1][list2[j]-2]==0:
            list3[list2[i]-1][list2[j]-2]=list3[list2[i]-1][list2[j]-1]+1
            #print([list2[i]-1],[list2[j]-2])
            #print(((list2[i]-1)*10)+(list2[j]-2),"hi")
            que.append(((list2[i]-1)*10)+(list2[j]-2))
        elif (list3[list2[i]-1][list2[j]-1]+1)<list3[list2[i]-1][list2[j]-2]:
            list3[list2[i]-1][list2[j]-2]=list3[list2[i]-1][list2[j]-1]+1
            que.append(((list2[i]-1)*10)+(list2[j]-2))
def short2(i,j):
    if i+1>=0 and i+1<n[0] and j>=0 and j<n[1]:
        k=list1[i+1][j]
        #print([list2[i]],[list2[j]-1],"hello")
        if k=='A':pass
        elif list3[i+1][j]==0:
            list3[i+1][j]=list3[i][j]+1
            que.append(((i+1)*10)+j)
            #print((list2[i]*10)+(list2[j]-1),"hi")
        elif (list3[i][j]+1)<list3[i+1][j]:
            list3[i+1][j]=list3[i][j]+1
            que.append(((i+1)*10)+j)
            #print((list2[i]*10)+(list2[j]-1),"hi")
    if i>=0 and i<n[0] and j+1>=0 and j+1<n[1]:
        l=list1[i][j+1]
        if l=='A':pass
        elif list3[i][j+1]==0:
            list3[i][j+1]=list3[i][j]+1
            que.append((i*10)+(j+1))
        elif (list3[i][j]+1)<list3[i][j+1]:
            list3[i][j+1]=list3[i][j]+1
            que.append((i*10)+(j+1))
    if i-1>=0 and i-1<n[0] and j>=0 and j<n[1]:
        m=list1[i-1][j]
        if m=='A':pass
        elif list3[i-1][j]==0:
            list3[i-1][j]=list3[i][j]+1
            que.append(((i-1)*10)+j)
        elif (list3[i][j]+1)<list3[i-1][j]:
            list3[i-1][j]=list3[i][j]+1
            que.append(((i-1)*10)+j)
    if i>=0 and i<n[0] and j-1>=0 and j-1<n[1]:
        n_1=list1[i][j-1]
        #print([list2[i]-1],[list2[j]-2],"hi")
        if n_1=='A':pass
        elif list3[i][j-1]==0:
            list3[i][j-1]=list3[i][j]+1
            #print([list2[i]-1],[list2[j]-2])
            #print(((list2[i]-1)*10)+(list2[j]-2),"hi")
            que.append((i*10)+(j-1))
        elif (list3[i][j]+1)<list3[i][j-1]:
            list3[i][j-1]=list3[i][j]+1
            que.append((i*10)+(j-1))
def short3(i,j):
    #print(i,j)
    if i+1>=0 and i+1<n[0] and j>=0 and j<n[1]:
        k=list1[i+1][j]
        #print([list2[i]],[list2[j]-1],"hello")
        if k=='D':pass
        elif dino[i+1][j]==0:
            dino[i+1][j]=dino[i][j]+1
            que.append(((i+1)*10)+j)
            #print((list2[i]*10)+(list2[j]-1),"hi")
        elif (dino[i][j]+1)<dino[i+1][j]:
            dino[i+1][j]=dino[i][j]+1
            que.append(((i+1)*10)+j)
            #print((list2[i]*10)+(list2[j]-1),"hi")
    if i>=0 and i<n[0] and j+1>=0 and j+1<n[1]:
        l=list1[i][j+1]
        if l=='D':pass
        elif dino[i][j+1]==0:
            dino[i][j+1]=dino[i][j]+1
            que.append((i*10)+(j+1))
        elif (dino[i][j]+1)<dino[i][j+1]:
            dino[i][j+1]=dino[i][j]+1
            que.append((i*10)+(j+1))
    if i-1>=0 and i-1<n[0] and j>=0 and j<n[1]:
        m=list1[i-1][j]
        if m=='D':pass
        elif dino[i-1][j]==0:
            dino[i-1][j]=dino[i][j]+1
            que.append(((i-1)*10)+j)
        elif (dino[i][j]+1)<dino[i-1][j]:
            dino[i-1][j]=dino[i][j]+1
            que.append(((i-1)*10)+j)
    if i>=0 and i<n[0] and j-1>=0 and j-1<n[1]:
        n_1=list1[i][j-1]
        #print([list2[i]-1],[list2[j]-2],"hi")
        if n_1=='D':pass
        elif dino[i][j-1]==0:
            dino[i][j-1]=dino[i][j]+1
            #print([list2[i]-1],[list2[j]-2])
            #print(((list2[i]-1)*10)+(list2[j]-2),"hi")
            que.append((i*10)+(j-1))
        elif (dino[i][j]+1)<dino[i][j-1]:
            dino[i][j-1]=dino[i][j]+1
            que.append((i*10)+(j-1))
n=list(map(int,input().split(" ")));list1=[];list2=[];list3=[];dino=[];k=0;l=0;m=0;n_1=0;que=[];first=[];second=[];third=[];renew1=[];renew2=[];count=0;count1=0
list2=list(map(int,input().split(" ")))
for i in range(n[0]):
    list1.append(list(input().split(" ")))
    list3.append(([0]*n[1]))
    dino.append(([0]*n[1]))
    renew1.append(([0]*n[1]))
    renew2.append(([0]*n[1]))
#print(list3)
for i in range(0,6,2):
    j=i+1
    list1[list2[i]-1][list2[j]-1]='A'
list1[list2[6]-1][list2[7]-1]='D'
#print(list1)
for i in range(n[0]):
    for j in range(n[1]):
        if list1[i][j]=='M':
            list3[i][j]=-1
            renew1[i][j]=-1
        if list1[i][j]=='W':
            list3[i][j]=-1
            dino[i][j]=-1
            renew1[i][j]=-1
            renew2[i][j]=-1
for i_1 in range(0,6,2):
    j_1=i_1+1
    short1(i_1,j_1)
    #print(i,j)
    print(que,list3,"hi")
    count=count+1
    print(count)
    while(len(que)!=0):
        num=que.pop(0)
        num1=num//10
        num2=num%10
        print(que,num1,num2)
        short2(num1,num2)
        print(list3)
    print("ko")
    if count==1:
        #print(renew1)
        first=copy.deepcopy(list3)
        list3=copy.deepcopy(renew1)
        print(list3,"copy1")
    if count==2:
        #print(renew1)
        second=copy.deepcopy(list3)
        list3=copy.deepcopy(renew1)
        print(list3,"copy2")
    if count==3:
        third=copy.deepcopy(list3)
        list3=copy.deepcopy(renew1)
        print(list3,"copy3")
print(first,second,third) 
short3(list2[6]-1,list2[7]-1)
while(len(que)!=0):
    num=que.pop(0)
    num1=num//10
    num2=num%10
    print(que,num1,num2)
    short3(num1,num2)
    print(dino)
print(dino,"hi")
for i in range(n[0]):
    for j in range(n[1]):
        if list1[i][j]=="G":
            if first[i][j]<dino[list2[0]][list2[1]]:
                count1=count1+1
