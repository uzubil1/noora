'''
def ascii_codes(a_string):
   
    for x in a_string:
       
        print(f"{x}:{ord(x)}")


def main():
   
    sample_string = "SWEC-123"
    ascii_codes(sample_string)

if __name__=="__main__":
    main()'''


def decode_ascii(ascii_codes_list):
    
    decoded_string = ''.join(chr(code) for code in ascii_codes_list)
    
    print(f"Decoded string: {decoded_string}")


def main():
    
    ascii_codes_list = [83, 87, 69, 67, 45, 49, 50, 51]  
    
    decode_ascii(ascii_codes_list)


if __name__=="__main__":
    main()
