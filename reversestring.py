def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        x= reverse_string(s[1:]) + s[0]
        return x
print(reverse_string("Hello"))

