n1=int(input('Enter the end value of the loop'))
n2=int(input('Enter the no. to be divisible'))
i=0
while i<n1:
    i+=1
    if i%n2!=0:
        continue
    print(i)
    
