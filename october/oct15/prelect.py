def discount(age):
    if age < 10:
        return 50
    elif  10 <= age < 19:
        return 30
    elif age >= 60:
        return 20
    else:
        return 0
    
def amount(tariff_standart, age):
    discount_percentage = discount(age)
    return tariff_standart * (1 - discount_percentage/100)

def main():
    child = 30
    twin = 20
    parent =35
    ages = [9, 16, 16, 40, 40]

    total_amount = 0

    for age in ages:
        if age == 9:
            total_amount+= amount(child, age)
        elif age == 16:
            total_amount+= amount(twin, age)
        elif age == 40:
            total_amount+= amount(parent,age)
        

        print("total amount to be paid by the family:", total_amount)


main()