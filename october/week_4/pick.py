

def check_guess(guess,answer):
    if guess == answer:
        return 0 #correct guess
    elif guess > answer:
        return guess - answer #guess is too high
    else:
        return answer - guess #guess is too low


import pytest
 
    

def test_check_guess_correct():
    assert check_guess(5, 5) == 0  # Correct guess

def test_check_guess_too_high():
    assert check_guess(8, 5) == 3  # Guess is 3 too high

def test_check_guess_too_low():
    assert check_guess(3, 5) == 2  # Guess is 2 too low



if __name__ == "__main__":
    test_check_guess_correct()
    test_check_guess_too_high()
    test_check_guess_too_low()
    print("All tests passed!")




