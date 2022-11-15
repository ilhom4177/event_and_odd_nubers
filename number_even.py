#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 1284
    
    
n1 = var_int%10
var_int = var_int//10

n2 = var_int%10
var_int = var_int//10

n3 = var_int%10
var_int = var_int//10

n4 = var_int%10 
var_int = var_int//10

#Print the number of even digits in the variable "var_int".

print(n1,n2,n3,n4  )