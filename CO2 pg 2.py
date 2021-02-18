#Generate Fibonacci series of N terms

n = int(input("Enter the limit : "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series : ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b