

def count_words(filename):
    
    word_counts = {} 
    
    try:
        with open(filename, 'r') as file:
            for line in file:
               
                words = line.split()  
                
                
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return {}
    
    return word_counts

def main():
   
    filename = "/Users/uzubil/noora/alice.txt"
    
   
    word_counts = count_words(filename)
    
    
    print("Top 10 most common words:")
    for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

