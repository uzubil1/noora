class Book:
    def __init__(self, title, author, num_pags):
        self.title = title
        self.author = author
        self.num_pags = num_pags

    def __str__(self):
        return self.title + ' by ' + self.author

    def __repr__(self):
        return "book(" + self.title + "," + self.author + "," + str(self.num_pags) + ")"
    
    def __lt__(self, other):
        return self.num_pags < other.num_pags
    
    def __gt__(self,other):
        return self.num_pags > other.num_pags #this is for true 
    
    def __eq__(self,other):
        if type(self) == type(other):
            return self.title == other.title and self.author and other.author
        else:
            return False
    
    def __ne__(self,other):
        return not self.__eq__(other) 
    
    def __hash__(self):
        return hash(self.title) * hash(self.author)
    
    def get_author(self):
        return self.author
    def set_num_pags(self,num_pags):
        self.num_pags = num_pags
        
def main():
    book_1 = Book("jungle book", "khalifa almari", 450)
    book_2 = Book("Harry Potter", "Rihan", 500)
    print(book_1)
    print(repr(book_1))
    print(book_1 < book_2)
    print(book_1 > book_2)
    print(book_1 == book_2)
    print(book_1 != book_2)
    print(book_1.get_author())
    book_2.set_num_pags(300)
    print(repr(book_2))
    print("hash code is:",hash(book_1))
if __name__ == "__main__":
    main()