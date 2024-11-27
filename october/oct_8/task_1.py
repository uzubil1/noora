
"""Task

1 - Create a text file with atleast 5 lines
2 - Read the file
3 - in the same program, write the text which u are reading from the file 1 to file 2"""


with open("kol.txt") as f:
    read = f.read()

    
    with open("new_kol.txt",'w') as g:
         g.write(read)

         