#lucas number
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    
    a,b = 2,1
    for i in range(n):
        a,b = b,a+b
    return b
  

print(lucas(5))