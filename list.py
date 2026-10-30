# #changing value in the list
# list1 = ['pysics','chemistry','1997','2000'];
# print("Value available at index 2")
# print(list1[2]);
# list1[2] = 2001;
# print("New value available at index 2 :")
# print(list1[2]);

# #deleting element fron the list
# del list1[2];
# print("After deleting value at index 2:")
# print(list1)

def comp(list2,list3):
    return list2 == list3
list2 = [45,56,35,6,5,75,45]
list3 = [34,43,34,34,212,12]

print(comp(list2,list3))
print(len(list2))
print(len(list3))

print(max(list2))
print(min(list3))