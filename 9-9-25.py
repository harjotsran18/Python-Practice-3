#write a program to show that a given number is even of odd

# a = int(input())
# if a%2==0:
#     print("Even number")
# else:
#     print("Odd number")    
     

age = int(input("Enter age:"))
day = str(input("Enter day of the week:"))    

baseprice = 200
if age<=3:
    price = 0
elif age>3 and age<=12:
    price = baseprice/2
    if day == "saturday" or day == "sunday":
        final_price = price - 50
    else:
        final_price = price
else:
    price = baseprice
    if day == "saturday" or day == "sunday":
        final_price = price - 50
    else:
        final_price = price
    # price = price
    # print("Price after day scnerio:",price)

    
    # final_price = final_price    
    print("Final fare: ",final_price)   
    