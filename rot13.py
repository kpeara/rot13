import sys
if len(sys.argv) == 2:
    file = open(sys.argv[1], "r")
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
                # is uppper case
            else:
                sr += i
        sr += '\n'
        rot13_lines.append(sr)

    print(lines)
    print(rot13_lines)

    file = open("rot13_" + sys.argv[1], "w")
    for i in rot13_lines:
        file.write(i)
    file.close()
