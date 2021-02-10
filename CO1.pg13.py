input_string = input("Enter the colours (speratted by comas):")
color_list  = input_string.split(",")
print( "%s %s"%(color_list[0],color_list[-1]))