"""same as task_1.py but functions"""

def read_file(filepath):
    with open("kol.txt") as f:
        read = f.read()
        print(read)
    return read  

def write(filepath):
    with open(filepath,'w') as g:
        data = read_file('kol.txt')
        g.write(data)

def main():
    write("kol2.txt")

main()