import sys

if len(sys.argv) == 2: # if a file is passed
    file = open(sys.argv[1], "r")
    rot13_lines = list()
    lines = file.readlines()
    file.close()

    for line in lines:
        sr = ""
        for i in line:
            if i != ' ':
                if i.islower():
                    asc = (ord(i) + 13) % 123
                    if asc < 97:
                        asc += 97
                    sr += chr(asc)

                elif i.isupper():
                    asc = (ord(i) + 13) % 91
                    if asc < 65:
                        asc += 65
                    sr += chr(asc)
            else:
                sr += i
        sr += '\n'
        rot13_lines.append(sr)

    #print(lines)
    #print(rot13_lines)
    file = open("rot13_" + sys.argv[1], "w")
    for i in rot13_lines:
        file.write(i)
    file.close()

else:
    print("Invalid number of arguments")

