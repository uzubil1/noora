def validate(user_id,password):
    user_s = "saf"
    password_s = "saf123"

    if user_id != user_s or password != password_s:
        raise ValueError("invalid user ID or password")

def login():
    attempts = 4
    while attempts > 0:
        user_id = input("enter user ID:")
        password = input("Enter password:")

        try:
            validate(user_id,password)
            print("Successful")
            return
        
        except ValueError as f:
            attempts -= 1
            print(f"{f} REmainig attempts: {attempts}")
            if attempts == 0:
                raise ValueError ("NO more attempts")
    

try:
    login()
except ValueError as f:
    print(f)