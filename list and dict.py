students_list= []
students_dict = {}

name=input("Enter Your Beautiful Name: ")
age=int(input("Enter Your Fruitful Age: "))
grade = int(input("Enter your grade: "))

students_list.append(name)
students_dict[ name ] = {'age':age, 'grade': grade}
print("Stuendt information added successfully!")

search_name = input("Enter the name you want to know: ")
if search_name in students_list:
    print(f"Name found!: {students_dict[search_name]}")
else:
    print("Name not Found!!!!")

remove_name = input("Enter the you want to remove or else skip: ")
if remove_name in students_list:
    students_list.remove(remove_name)
    del students_dict[remove_age,grade]
    print("Name removed successfully")
    print("Name availiable: ", students_list)
else:
    print("Book not found")