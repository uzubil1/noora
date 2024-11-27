"""This code simply adds the numbers written on each line of a txt file
Please note that it only adds one number per line
"""

def readFile(fileNm):
    total=0
    try: 
        with open(fileNm, 'r') as file1:
            
            for line in file1:
                strippedLine= line.strip()
                number= int(strippedLine)
                total= total+ number
            print(total)
    except:
        print("There can be file not found or other errors")
    

def main():
    fileName=input("Enter file name along with its path: ")
    readFile(fileName)
    
main()
    
    