name=str(input("Enter Your Name:"))
print("1. Addition")
print('2.Subtraction')
print("3. Multiplication")
print("4. Divison")
missing_value_choice = input("Enter the option number for the missing value:")

if missing_value_choice == "1":
    num1= float(input("num1 :"))
    num2= float(input("num2:"))
    Sum= num1+num2
    print(f"Sum = {Sum})")

elif missing_value_choice == "2":
    num1= float(input("num1 :"))
    num2= float(input("num2:"))
    Dif= num1-num2
    print(f"Dif = {Dif})")

elif missing_value_choice == "3":
    num1= float(input("num1 :"))
    num2= float(input("num2:"))
    Product= num1*num2
    print(f"Product = {Product})")

elif missing_value_choice == "4":
    num1= float(input("num1 :"))
    num2= float(input("num2:"))
    dividant= num1/num2
    print(f"dividant = {dividant})")

else:
    print('Invalid Value assigned')