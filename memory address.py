def finding_repeating_number(i):
    character_count= {}
        #Iterating through the characters in the string
    for character in i:
        #Chceh if the character already encountered
        if character in character_count:
            print(f"The memory address of the first repeating character '{character}' is : {id(character)}")
            return character, id(character)
        else:
            character_count[character] = 1
    return None
x = input("What is your favourite number: ")
y = finding_repeating_number(x)
if y is None:
    print("No repeating character found.")