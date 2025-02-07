fb = open("text", "r")
print(fb.read())
fb.close() # close is a good practie, not needed when doing the read method. Works just as fine with or without

# same thing, but more pythonic

with open("text", "r") as fb:
    print(fb.read())


print("we are done, the context is closed by the indent")

# read from the same file, line by line
with open("text", "r") as fb:
    line_number = 1
    for line in fb:
        print(line, end="") # since there is already lines in the text file, we can tell python to not end with nothing
        print(f"{line_number}:{line.rstrip()}") 
        line_number += 1
