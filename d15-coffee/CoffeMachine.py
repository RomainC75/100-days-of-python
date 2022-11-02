# TODO: 2. check ressources

class CoffeeMachine:
    def __init__(self):
        self.menu = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def getPrice(self, name):
        if ( name in self.menu.keys() ):
            return self.menu[name]["cost"]
        return False

    def getResources(self):
        return self.resources

    def canServeCoffe(self, name):
        if ( name in self.menu.keys() ):
            for key in self.menu[name]['ingredients'].keys():
                if(self.resources[key] < self.menu[name]['ingredients'][key]):
                    return key
            return True
        return False

    def serveCoffe(self, name):
        if ( name in self.menu.keys() ):
            for key in self.menu[name]['ingredients'].keys():
                if(self.resources[key] >= self.menu[name]['ingredients'][key]):
                    self.resources[key]-=self.menu[name]['ingredients'][key]
            return self.resources
        return False
