x=int(input("Enter your age: "))
y=input("Are you a student? Yes/No: ")
if  x <= 12 :
    print("You are eligble for a discount on the movie ticket")
elif x >= 13 and x <= 18 and y == " Yes":
    print("You are eligible for a discount on the movie ticket")
else:
    print("you are not eligble for a discount in the movie ticket")