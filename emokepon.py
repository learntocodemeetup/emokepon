import random

opponents = ["Pikachu", "Bulbasaur", "Charmander"]

class Pokemon():

    gotta_catch_em_all = "Yes you do."

    def __init__(self, colour):
        self.health_points = random.randint(1,10)
        self.colour = colour

    def attack(self):

        opponent = random.choice(opponents)
        print("You attacked:", opponent)

        self.health_points -= 2
        print("Their health points are:", self.health_points)
        print("")

        if self.health_points <= 0:
            print("Peeka pee :(")
        else:
            print("Pi ka chu!")

pikachu = Pokemon('yellow')
bulbasaur = Pokemon('green')
charmander = Pokemon('red')

pikachu.gotta_catch_em_all = "No"
bulbasaur.gotta_catch_em_all = "Bul ba sire!"

print("Welcome to Emokepon")
print("")

print("Pikachu's hit points are:", pikachu.health_points)
print("Bulbasaur's hit points are:", bulbasaur.health_points)
print("Charmander's hit points are:", charmander.health_points)
print("")
# Looks at Pikcahu's health points and substracts 2 each time

count = 0

while True:
    pikachu.attack()
    bulbasaur.attack()
    charmander.attack()

    count += 1

    if count >= 10:
        break

# print("Pikachu's colour is:", pikachu.colour)


# print("Bulbasaur's colour is:", bulbasaur.colour)

# print("Do you gotta catch em all?", pikachu.gotta_catch_em_all)
# print("Do you gotta catch em all?", bulbasaur.gotta_catch_em_all)
# print("Do you gotta catch em all?", charmander.gotta_catch_em_all)
