
import random

class pet(): 
    def __init__(self,name,money,inventory,happiness,satiety,poo,health,cleanliness,strength):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happiness
        self.satiety = satiety
        self.poo = poo
        self.health = health
        self.cleanliness = cleanliness
        self.strength = strength

    def buy(self, item):
        self.inventory.append(item)
        
        print("this is what you have in your inventory:")
        for i in self.inventory:
            print(i["name"])
        print("you have", self.money, "dollars left")

    def feed(self):
        self.satiety += 100
        self.happiness +=10
        self.poo +=100
        print("your pet,", self.name, "is fed to", self.satiety, "satiety, but he needs to poop", self.poo, "%")
    
    def poop(self):
        self.poo = 0
        print(self.name, "has pooped, and he is at", self.poo, ("% poop"))
        self.cleanliness +=50

    def accident(self):
        self.poo = 0
        print(self.name, "has pooped all over your carpet, and he is at", self.poo, ("% poop"))
        self.cleanliness -= 60
    
    def clean(self):
        self.cleanliness +=70
        print("you have cleaned the house from its poop")
    def noclean(self):
        self.cleanliness = 0
        self.health = 0
        print(self.name, "has contracted salmonella")
    
    def putdown(self):
        self.health = 0
    
    def display_info(self):
        print("Name:", self.name, "Money:", self.money, "Happiness:", self.happiness, "Satiety:", self.satiety, "Poop meter:", self.poo, "health:", self.health, "cleanliness", self.cleanliness)
    
    def play(self):
        self.happiness +=50
        print("wow your pet", self.name, "is now at", self.happiness, "happiness")
    
    def train(self):
        self.strength +=4
        print("your pet is now at", self.strength, "strength")

class attacker():
    def __init__(self,attack,health):
        self.attack = attack
        self.health = health
    def attac(self):
        Poopyguy.health -= self.attack
        print("the attacker has attacked your pet, and your pet is now at", Poopyguy.health, "health")
    def showstat(self):
        print("attacker health:", self.health, "attacker attack:", self.attack)

Poopyguy = pet("poopguy", 20, [{"name": "poop"}],50,50,50,100,100,0)
attackerer = attacker(random.uniform(1,10),random.uniform(1,100))

while Poopyguy.health > 0:

    stating = input("do you want to check your pets stats? (yes/no) ")
    if stating == "yes":
        Poopyguy.display_info()

    buy = input("do you want to buy somethign (yes/no)")
    if buy == "yes":
        Poopyguy.buy({"name": "stick", "atk": 2, "price": 20})

    play = input(f"do you want to play with {Poopyguy.name}")
    if play == "yes":
        Poopyguy.play()

    fed = input("do you want to give it food (yes/no) ")
    if fed == "yes":
        Poopyguy.feed()

    if Poopyguy.poo > 100:
                Poopyguy.health -= 2
                print("yo poopyguy is dying because he has too much poop in his butt")

    if Poopyguy.poo >50:
        pooo = input("do you want to take him to poop (yes/no) ")
        if pooo == "yes":
            Poopyguy.poop()
        elif pooo == "no":
            Poopyguy.accident()
            clean = input("do you want to clean it and the house from this poop? (yes/no) ")
            if clean == "yes":
                Poopyguy.clean()
            if clean == "no":
                Poopyguy.noclean()

    if Poopyguy.satiety <=0:
        Poopyguy.health -= 5
        print("you need to feed poopyguy he is dying ")

    traininging = input("do you want to train your pet ")
    if traininging == "yes":
        Poopyguy.train
    putdowning = input("do you want to put its poor life down")
    if putdowning == "yes":
        Poopyguy.putdown()

    Poopyguy.satiety -=5
    Poopyguy.happiness -=5
    battle = 6

    if battle == 6:
        print("oh no another animal is attacking your pet:")
        while attackerer.health > 0 and Poopyguy.health > 0:
            fart = 1*(1+(Poopyguy.strength/100))
            slash = 4*(1+(Poopyguy.strength/100))
            punch = 3*(1+(Poopyguy.strength/100))
            attackerer.showstat()
            attackerer.attac()
            atick = input("what do you want to hit him with? (fart,slash,punch)")
            bleed = 0
            if atick == fart:
                attackerer.health -= fart
            elif atick ==slash:
                attackerer.health -= slash
                bleed = 5
            if bleed >= 3:
                attackerer.health -=1
                bleed -=1
            if atick == punch:
                attackerer.health -= punch
            
if Poopyguy.health <=0:
    print(Poopyguy.name, "is dead")
if Poopyguy.happiness < 0:
    print("yo poopyguy is getting sad i think you should put him down or make him happier")

