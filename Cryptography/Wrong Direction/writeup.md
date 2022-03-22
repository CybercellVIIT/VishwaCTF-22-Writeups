Title: Wrong Direction

Flag: VishwaCTF{5ay_h1_3nc0d1n9}

By Extracting the tar file a structure of nested folders can be found. Each folder contains a suspesious file. 

The filenames are some encoded string or chiphers of a youtube link to get RickRoll. 
Inside every file there are digits containing 0's and 1. Each file contains only one 1 and others are 0's

If noticed carefully the number of digits inside a file is equal to the numgber of char in file name. Suggesting it has something to do with the file name.

By using a Python script a string can be made using a char from the file name corresponding to the position of 1 in the same file.

Here could be the sample script.

```
import os

chipher = ""

base = "1"

while True:
    names = os.listdir(base)

    if len(names)==0:
        break

    if len(names[0]) <3:
        diret = names[0]
        fname = names[1]
    else:
        diret = names[1]
        fname = names[0]    

    name = f"{base}/{fname}"
    with open(name, 'r') as file:
        text = file.readline()
        where = text.find("1")
        letter = fname[where]
        chipher += letter
        base += f"/{diret}"

print(chipher)

```

By the script we get a string `<bZVgG@<j<7XI"$H!b5>?ScS00OunU3IL`

Looking at this carefully, presence of few chars indicates that the string actully is base85 encoded string. 

By Decoding the string from Base85 the flag can be found.
