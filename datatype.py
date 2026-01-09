#Declear data type

name = "Akash "
lastname = "pandey"
age = 21    #integer
height = 5.4
weight = 40.60
year = 2025
phone = 9587462458
x = 8
y = "15"     #string

#print the type of data

print(type(name))
print(type(lastname))
print(type(age))
print(type(height))
print(type(weight))
print(type(year))
print(type(phone))

#Add two varibale of same datatypes

print(age+year)
print(name+lastname)
print(height+weight)

#Add two variable of different datatypes

z = int(y)       #convert string into int.
A = str(age)     #convert int. into str.
B = float(age)   #convert int. into float
print(x+z)
print(name+A)
print(height+B)

#Boolean

k = 7
l = 11
print(k>l)
print(l>k)