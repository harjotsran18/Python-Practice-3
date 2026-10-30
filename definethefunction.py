def fun(Name):
    print(Name)
fun("Harjot")    

print("\n")

#keyword arguments
def my_funtion(sub1,sub2,sub3):
    print("The easiest subject is:" +sub3)
my_funtion(sub1 = "IWT" , sub2 = "DECA" , sub3 = "PYTHON") 

print("\n")

#passing list as an arguements
def my_function(food):
    for x in food:
        print(x)
        
fruits = {"apple","banana","cherry"}
my_function(fruits)   

print("\n")

#return value
def my_function(x):
    return 5*x
print(my_function(5))
print(my_function(3)) 