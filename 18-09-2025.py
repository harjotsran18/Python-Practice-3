#largest number
a = [95,6,65,65,662,23,654,996]
largest = max(a)
print("Largest number : ",largest)

#reverse the list
list = ["a","b","c","d"]
rev_list = []
for i in range(len(list) -1,-1,-1):
    rev_list.append(list[i])
print(rev_list)    

#Count Occurrences of an Element 
list = ["a","a","b","c","a"]
count = list.count("a")
print(count)

#Remove Duplicates from a List
list1 = ["a","b","c","a"]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("List : ",list2)         

#palindrome number
number = 12321
original_number = 12321
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10  # Remove the last digit from the number

if reversed_number == original_number:
    print("Yes")
else:
    print("no") 