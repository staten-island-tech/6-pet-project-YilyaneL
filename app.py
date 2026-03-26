class pet():
    def __init__(self,name,money,health,happiness,satiety):
        self.name = name
        self.money = money
        self.health = health
        self.happiness = happiness
        self.satiety = satiety

    def putitdown(self,health):
        ptdwn = input("doy ou want to put your pet down? (yes/no) ")
        if ptdwn == "yes":
            ogpet.health = 0
            print("your pet", ogpet.name, "is DEAD ")

    def feedit

newpet = input("make a new pet (name) ")
ogpet = pet(newpet, 0, 100, 50, 70)

pet.putitdown(ogpet,100)
