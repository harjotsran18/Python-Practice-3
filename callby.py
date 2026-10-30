#call by value

def myfunc(a):
    print("\tValue received in 'a'  = ",a)
    a+=2
    print("\tValue of 'a' changes to : ",a)
    
num = 13
print("Initial number: ",num)
myfunc(num)
print("Value of number = ",num)  

print("\n\n")
#Call by reference
def myfun(x):
    x[0] = 20
    
lst = [10,11,12,13,14,15]
myfun(lst)
print(lst)         

 