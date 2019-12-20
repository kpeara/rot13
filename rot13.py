import sys

file = open("input.txt", "r")
# take param as any file and generate filename_rot13
rot13_lines = list()
lines = file.readlines()
file.close()

for line in lines:
    sr = ""
    for i in line:
        if i != ' ':
            if i.islower():
                asc = (ord(i) + 1) % 123
                if asc < 97:
                    asc + 97
                sr += chr(asc)
        else:
            sr += i
    sr += '\n'
    rot13_lines.append(sr)

print(lines)
print(rot13_lines)

file = open("rot13_input.txt", "w")
for i in rot13_lines:
    file.write(i)
