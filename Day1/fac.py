n = int(input('Enter number'))

j=0
i=1
while (i<=n):
    if (n%i==0):
        print(i)
        j+=1
       
    i+=1
        
print("Number of factors of "+str(n)+":"+str(j))

