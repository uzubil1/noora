"""
This program is about taking the birthdates from user 3 times
This contains 1 function    
    
"""

def user_birthday():
    '''
    This function takes 4 inputs
    and prints the values
    '''
    name1= input("Please write your name")
    birthMonth1= input("Please type your Birth Month")
    birthDay1= input("Please type your Birth Day of the Month")
    birthYear1= input("Please type your Birth Year")

    # "Albus, your birthday is on July 10, 1881!"

    print(name1, ", your birthday is on",birthMonth1,birthDay1, ", " , birthYear1, "!")
    
    
def main():
    user_birthday()  # this is calling of the function
    user_birthday()
    user_birthday()
    
main()





