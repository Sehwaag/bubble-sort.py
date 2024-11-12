num=[5,7,3,6,9,1]
for i in  range(len(num)-1):
    for j in range(len(num)-1-i):
       if(num[j]>num[j+1]):
        
           temp=num[j]
           num[j]=num[j+1]
           num[j+1]=temp
           print(num)
print(num)
