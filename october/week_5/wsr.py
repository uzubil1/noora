

def wordsearch(file):
    f=open(file,"r")
    read = f.read()
    f.close
    word = input("enter the word to be searched:")
    detector = 0
    words=read.split()
    for i in words:
        if i == word:
            print("word was founf:", i)
            detector = 1
    if detector ==0:
        print("word not found!")

def main():
    file = input("enter file name:")
    wordsearch(file)        


main()