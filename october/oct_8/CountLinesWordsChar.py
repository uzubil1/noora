
"""This python code will read a text file 
count its lines
count itys words
and then count its total charachters
"""

def count_lines_words_Chars(filePath):
    #i need to open the file for reading
    with open(filePath, "r") as f:

        lineCount = 0
        wordCount = 0
        charCount = 0

        for line in f:
            #line count
            lineCount = lineCount + 1

            #words count
            StrippedWords = line.strip() #remove extra spaces
            words = StrippedWords.split() # split the words on every line
            wordCount = wordCount + len(words)

            #characters Count
            charCount = charCount + len(line)
            #print(len(line)) for counting characters
            #print(line) #if i want to remove space "line.strip()"

        print("line counts:", lineCount)
        print("words counts:", wordCount)
        print("Characters counts:", charCount)


def main():
    filePath = "sample.txt"
    count_lines_words_Chars(filePath)

if __name__ == "__main__":
    main()