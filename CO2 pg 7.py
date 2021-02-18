#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’

string = str(input("Enter the string : ")) 
if len(string) < 3:
  print(string)
elif string[-3:] == 'ing':
  print(string + 'ly')
else:
  print(string + 'ing')