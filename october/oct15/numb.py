


def numb(filename):
    total_sum = 0 
    with open(filename, 'r') as file:
        for line in file:
            total_sum += int(line.strip())
    print(f"Sum of numbers: {total_sum}")


numb('number.txt')