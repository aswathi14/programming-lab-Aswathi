#Generate a list of four digit numbers in a given range with all their digits even and the  number is a perfect square. 

from math import sqrt as s
n=int(input("Enter a limit:"))
p=0
for i in range(1000,n):
    if s(i)==int(s(i)) and i%2==0:
        print(i)


