#Count the number of characters (character frequency) in a string. 

test_str=str(input("Enter the string : ")) 
freq = {} 
  
for i in test_str: 
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1
  
print ("Count of all characters :\n "+  str(freq))