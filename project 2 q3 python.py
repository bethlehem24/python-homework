
#3) Manipulating lists
        # You may be familiar with adding individual data elements to a list by using the .append() method. However, if you want to combine a list with another array type(list, set, tuple), you can use the .extend() method on the list.
        # You can also use the .index() method to find the position of an item in a list. You can then use that position to remove the item with the .pop() method.
        # In this exercise, you'll practice using all these methods!
        # Ask 4 students at Datanomics to enter their names one at a time
        # Add their names to the list

# Ask 4 students to enter their names

student_names = []
for i in range(4):
    name = input(f"Enter the name of student {i+1}: ")
    student_names.append(name)

# Extend the list with two additional new students
print("Adding two more new students.")
student_names.extend(['Rediet', 'Haim'])

# Print the updated list of student names
print("Student names after adding new students:", student_names)

# Ask which student to find in the list
student_to_remove = input("Enter the name of the student you want to remove: ")

# Find the position of the student and store it in a variable
if student_to_remove in student_names:
    position = student_names.index(student_to_remove)
    
    # Remove the student from the list using the .pop() method
    student_names.pop(position)

    # Print the final list of student names
    print("Student names after removing one student:", student_names)
else:
    print(f"Student '{student_to_remove}' is not in the list.")
