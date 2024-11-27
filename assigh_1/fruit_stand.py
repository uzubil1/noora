class Fruit:
    def __init__(self, type, price, season):
        self.type = type    
        self.price = price  
        self.season = season

    


APPLE = Fruit("Apple", 1.35,"spring")
PEACH = Fruit("PeaCH", 1.20,"spring")
ORANGE = Fruit("Orange", 0.99, "winter")



print(f"{APPLE.type} costs ${APPLE.price}")
print(f"{PEACH.type} costs ${PEACH.price}")
print(f"{ORANGE.type} costs ${ORANGE.price}")


