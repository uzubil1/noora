class Animal:
    def __init__(self, animalName, animalAge):
        self.name = animalName
        self.age = animalAge


def main():
    cat = Animal(animalName ="sunny",animalAge = 4 )
    print(cat.name, cat.age)


if __name__ == "__main__":
    main()