class pet():
    def __init__(self,name,money,inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        
        print("this is what you have in your inventory:")
        for i in self.inventory:
            print(i["name"])
        print("you have", self.money, "dollars left")

Poopyguy = pet("poopguy", 20, [{"name": "poop"}])

buy = input("do you want to buy somethign (yes/no)")

if buy == "yes":
    Poopyguy.buy({"name": "stick", "atk": 2, "price": 20})

