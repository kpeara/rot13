file = open("input.txt", "r")
# take param as any file and generate filename_rot13

text = file.readlines()
text_list = list(text) # lists in python are immutable
sr = ""

print(text[0])
for i in text[0]:
    if i != ' ':
        if i.islower():
            asc = (ord(i) + 1) % 123
            if asc < 97:
                asc + 97
            sr += chr(asc)
    else:
        sr += i

print(sr)
