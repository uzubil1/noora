# /Users/uzubil/noora/myCSVFILE.CSV
import csv 

def readCSV(filepath):
    with open(filepath, 'r') as f:
        CSVReader =csv.reader(f)

        for line in CSVReader:
            print(line)





def main():
    filepath = "/Users/uzubil/noora/myCSVFILE.csv"
    readCSV(filepath)

if __name__ == "__main__":
    main()