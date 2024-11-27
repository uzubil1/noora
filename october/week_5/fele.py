
def tokenizer(inputstring, delimiter):
    tokens = inputstring.split(delimiter)
    return tokens


messageString = "Greetings! i|am|a|gcis|123 student"
delimiter = "|"
x = tokenizer(messageString, delimiter)
for token in x:
    print(token)

tokenizer()