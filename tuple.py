# my_tuple = (10,20,30,40)
# ma = max(my_tuple)
# print(ma)
# mi =  min(my_tuple)
# print(mi)


#score
print("PROGRAM 1")
scores = (56, 78, 45, 89, 90, 67, 72, 100, 34)
print("Maximum score: ",max(scores))
print("Minimum score: ",min(scores))
print("Length of score: ",len(scores))
print("Average score: ",sum(scores)/len(scores))
print("No.of students who scored above 70: ",sum(1 for x in scores if x > 70))

print("\n\nPROGRAM 2")
#employes
employees = (
    (101, "Amit", "HR", 45000, 2018),
    (102, "Neha", "IT", 65000, 2020),
    (103, "Ravi", "Finance", 55000, 2019),
    (104, "Sneha", "IT", 70000, 2021),
    (105, "Karan", "Marketing", 40000, 2017),
    (106, "Pooja", "Finance", 60000, 2022)
)
print("No. of employees: ",len(employees))
print("Maximum salary: ",max(employees, key=lambda employees: employees[3]))
print("Minimum salary: ",min(employees, key=lambda employees: employees[3]))