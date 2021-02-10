w=input("Enter a string separted with space:")
s=w.split(" ")
print("let swap the string")
for i in reversed(range(0,len(s))):
    print(s[i],end=" ")
