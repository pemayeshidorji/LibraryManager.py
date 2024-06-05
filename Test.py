print("Newton's Second law of motion")
print("----------------------------------------------")

print('Select the missing value:')
print ("1. mass (m)")
print ("2. Acceleration(a)")
print("3. Force(F)")
missing_value_choice = input("Enter the option number for the missing value:")

if missing_value_choice == "1":
    a= float(input("Enter acceleartion (a) :"))
    F= float(input("Enter Force (F):"))
    m = F/a
    print(f"Maass (m) = {m})")

elif missing_value_choice == "2":
    m= float(input("Enter mass (m) :"))
    F= float(input("Enter Force (F):"))
    a = F/m
    print(f"acceleartion (a) = {a})")

elif missing_value_choice == "2":
    a= float(input("Enter acceleartion (a) :"))
    m= float(input("Enter mass (m):"))
    F= m*a
    print(f"force (F) = {F})")

else:
    print("Invalid option selected for the missing value.")

