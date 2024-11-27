


'''Prompt the user to input a string of semi-colon-seperated vegetable-cost pairs (formatted as
vegetable_name:cost:quantity)
After each entry, the total cost of all vegetables (cost x quantity) should becalculated and printed
if the input is "done" the function should terminate and print "Program terminated."
raise a ValueError if the nput format is incorrect'''



""""def vegetable_cost_calculator():
    total_cost = 0
    while True:
        x = input("Enter a vegetable-cost-pairs quantity (done to end)")
        if x == 'done':
            print("Program terminated")
            break
        vegetable_cost_pairs = x.split(';')
        for pair in vegetable_cost_pairs:
            try:
                each_vegetable = pair.split(":")
                cost = float(each_vegetable[1].strip())
                quantity = float(each_vegetable[2].strip())
                total_cost = total_cost + cost * quantity
                print(f"Total cost is: {total_cost}")
            except ValueError:
                print("Value not found!")
            """



'''
def vegetable_cost_calculator():
    total_cost=0.0
    while True:
        user_input = input("Enter vegetable cost quantity pairs: (or done to terminate)")
        if user_input == "done":
            print("Program terminated")
            break
        vegetable_cost_pairs = user_input.split(';')
        for pair in vegetable_cost_pairs:
            try:
                each_vegetable = pair.split(":") # split the vegetable, cost, and quantity
                cost = float(each_vegetable[1].strip())
                quantity = float(each_vegetable[2].strip())
                total_cost += cost * quantity
            except ValueError:
                print("Value not found!")
        print(f"Total cost is: {total_cost}")
vegetable_cost_calculator()'''



def vegetable_cost_calculator():
    total_cost = 0
    while True:
        x = input("Enter vegetable-cost-quantity pairs (format: name: cost: quantity, separated by ';') or type 'done' to end: ")
        if x.lower() == 'done':
            print("Program terminated")
            break
            
        vegetable_cost_pairs = x.split(';')
        for pair in vegetable_cost_pairs:
            try:
                each_vegetable = pair.split(";")
                name = each_vegetable[0].strip()
                cost = float(each_vegetable[1].strip())
                quantity = float(each_vegetable[2].strip())
                total_cost += cost * quantity
            except (ValueError, IndexError):
                print(f"Invalid input for pair '{pair}'. Please use the correct format.")
        
        print(f"Total cost so far is: {total_cost}")

vegetable_cost_calculator()
