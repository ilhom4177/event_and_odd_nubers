#A four-digit integer is given. Find the number of even digits in it.
def var_int(var_int):
#Create a variable "var_int" and assign it a four-digit integer value.
    

    a = var_int%10
    a1 = (a%2+1)%2
    var_int//=10

    b = var_int%10
    b1 = (b%2+1)%2
    var_int//=10

    c = var_int%10
    c1 = (c%2+1)%2
    var_int//=10

    d = var_int%10
    d1 = (d%2+1)%2

    return a1+b1+c1+d1
print(var_int(1304))

#Print the number of even digits in the variable "var_int".

