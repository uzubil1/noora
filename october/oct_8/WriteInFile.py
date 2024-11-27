

"""This python code will line some text content
in a text file"""
"""Remember the following while writing in a file 
1 - Dont forget to write the 'w' mode
2 - Even if you  dont create the file in path, it will create a new file for u"""

def write_in_file(filepath,multilines):
    with open(filepath, 'w') as f: #if i want to add smth without remove anything i should replace 'w' to 'a' and change the phrase in ()
        for line in multilines:
            f.write(line + "\n")
       # f.write("This is a sunny day " + "\n") #for space between phraces add + "\n"

def main():
    filepath = "File08102024.txt"
    multilines = ["my name is Saf","i am in GCIS123", "this is section 601"]
    write_in_file(filepath,multilines)

if __name__ == "__main__":
    main()
    