#grocery list
grocery = ["pulses","maggie","pasta","milk","eggs"]
print("\nIninial grocery list : ", grocery)

print("\nFirst item : ",grocery[0])
print("Last item : ",grocery[-1])

print("\nSliced list : " , grocery[1:4])

grocery.append("fruits")
print("\nAppended list : ",grocery)

# grocery.extend("eggs")
# print("\nAfter extend : ",grocery)

grocery.insert(5,"cheese")
print("\nAfter inserting : ",grocery)

index_of_milk = grocery.index("milk")
print("\nIndex of milk : ",index_of_milk)

grocery.append("maggie")
fruit_count = grocery.count("maggie")
print("\nCount of Maggie : ",fruit_count)

grocery.sort()
print("\nSorted list : ",grocery)

grocery.reverse()
print("\nReversed list : ",grocery)

popped_item = grocery.pop()
print("\nPopped Item:", popped_item)
print("After Pop:", grocery)

nested_grocery_list = [
    ["Fruits", ["Apples", "Bananas", "Tomatoes"]],
    ["Dairy", ["Milk", "Cheese"]],
    ["Bakery", ["Bread"]]
]
print("\nNested Grocery List:")
for i in nested_grocery_list:
    print(f"{i[0]}:{i[1]}")
    
    
#books
books = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "the ruler"]
print(books[0])
print(books[:2])


books.append("Pride and Prejudice")
print(books)
books.extend(["The Catcher in the Rye", "Jane Eyre"])
print(books)
books.insert(3, "Brave New World")
print(books)


print(books.index("the ruler"))
print(books.count("1984"))


books.sort()
print(books)
books.reverse()
print(books)


removed_book = books.pop(2)
print(removed_book)


book_collection = {
    "Classics": ["1984", "Pride and Prejudice", "Jane Eyre"],
    "American Literature": ["To Kill a Mockingbird", "The Catcher in the Rye", "The Great Gatsby"],
    "Dystopian": ["Brave New World", "the ruler"]
    }

print("\n Book Collection by Genre:")
for genre, titles in book_collection.items():
    print(f"{genre}: {', '.join(titles)}")

students = ["Ali", "heaven", "John", "Mehak", "harjot"]


print(students[0])
print(students[-2:])


students.append("Ayesha")
print(students)
students.extend(["Bilal", "Tina"])
print(students)
students.insert(2, "Hamza")
print(students)


print(students.index("heaven"))
print(students.count("Ali"))


students.sort()
print(students)
students.reverse()
print(students)


left_student = students.pop()
print("Student who left:", left_student)


student_groups = {
     "Class A": ["Ali", "heaven", "Hamza"],
     "Class B": ["John", "Mehak", "harjot"],
    "Class C": ["Ayesha", "Bilal", "Tina"]
 }

print("\n Students by Class:")
for class_name, names in student_groups.items():
     print(f"{class_name}: {', '.join(names)}")