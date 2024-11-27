def longest_word(string):
    read=string.split()
    j=""
    count=0
    for i in read:
        if len(i)>count:
            j=i
            count=len(i)
    print("the longest word is:",j)


def longest_words(filename):
    f=open(filename,"r")        
    read = f.readlines()
    f.close
    for i in read:
        longest_word(i)

def main():
    filename=input("enter file name:")
    longest_words(filename) 

main()
