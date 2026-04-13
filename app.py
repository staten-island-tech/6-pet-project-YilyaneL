class pet():
    def __init__(self,name,money,inventory,happiness,satiety,poo,health,cleanliness):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.happiness = happiness
        self.satiety = satiety
        self.poo = poo
        self.health = health
        self.cleanliness = cleanliness

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
        self.satiety = 0
        print(self.name, "has pooped, and he is at", self.poo ("% poop"))
        self.cleanliness +=50

    def accident(self):
        self.satiety = 0
        print(self.name, "has pooped all over your carpet, and he is at", self.poo, ("% poop"))
        self.cleanliness -= 60
    
    def clean(self):
        self.cleanliness = 100
        print("you have cleaned the house from its poop")
    def noclean(self):
        self.cleanliness = 0
        self.health = 0
        print(self.name, "has contracted salmonella and")
    
    def putdown(self):
        self.health = 0
    
    def display_info(self):
        print(f"Name: {self.name}, Money: {self.money}, Happiness: {self.happiness}, Satiety: {self.satiety}, Poop meter: {self.poo}, health: {self.health}, cleanliness {self.cleanliness}")
        
Poopyguy = pet("poopguy", 20, [{"name": "poop"}],50,0,0,100,100)

while Poopyguy.health > 0:

    buy = input("do you want to buy somethign (yes/no)")
    if buy == "yes":
        Poopyguy.buy({"name": "stick", "atk": 2, "price": 20})

    fed = input("do you want to give it food (yes/no) ")
    if fed == "yes":
        Poopyguy.feed()
    if Poopyguy.poo >50:
        pooo = input("do you want to take him to poop (yes/no) ")
        if pooo == "yes":
            Poopyguy.poop()
        elif pooo == "no":
            Poopyguy.accident()
            clean = input("do you want to clean it and the house from tis poop? (yes/no) ")
            if clean == "yes":
                Poopyguy.clean()
            if clean == "no":
                Poopyguy.noclean()
    putdowning = input("do you want to put its poor life down")
    if putdowning == "yes":
        Poopyguy.putdown()
    stating = input("do you want to check your pets stats? (yes/no) ")
    if stating == "yes":
        Poopyguy.display_info()
if Poopyguy.satiety <=0:
    Poopyguy.health -= 5
    print("you need to feed poopyguy he is dying ")
if Poopyguy.health <=0:
    print(Poopyguy.name, "is dead")

