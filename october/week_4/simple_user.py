# sum of numbers from 1 to 5 using while loop




#print even numbers from 0 to 10 using while loop



#simple user

##while input1!= "x":
    #input1= input("Enter a string;")

input1=""
'''while True:
    input1=input("enter something:")
    if input1=="x":
        break
print("Exiting the loop...")'''


while True:
    input1=input("Enter something:")
    if input1=="y":
        #print("you entered y") #without this stroke everything but Y wil be accepted
        continue
    print(input1)
    if input1=="x":
        break
print("exiting the loop..")