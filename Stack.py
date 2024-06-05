from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

#Visit Function
NoofVisists = int(input("Enter the number of url history : "))
print("Enter URLs to visit:")
for i in range(NoofVisists):
    url = input("URL: ")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url

#Displaying current Page
print(f"Current page {current_page}")

#Go Back
while input("Do you want to go back? (yes/no):").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page avaliable")

#Go Forward
while input("Do you want to go forward? (yes/no):").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page avaliable")

