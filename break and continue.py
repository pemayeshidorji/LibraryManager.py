for i in range(9):
    if i == 3:
        print("The number 3 has been skipped")
        continue
    elif i==7:
        print("The outer loop is now broke")
        break
        for y in range(3):
            continue
    print(i)