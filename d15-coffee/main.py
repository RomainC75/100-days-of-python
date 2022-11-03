# TODO: 1. print prompt
from CoffeMachine import CoffeeMachine

def getMoney():
    total=0
    try:
        total += int(input('number of 0.25 :'))*0.25
    except:
        total+=0

    try:
        total += int(input('number of 0.10 :'))*0.10
    except:
        total+=0

    try:
        total += int(input('number of 0.05 :'))*0.05
    except:
        total+=0

    try:
        total += int(input('number of 0.01 :'))*0.01
    except:
        total+=0

    return total


if __name__ == '__main__':
    print('PyCharm')

    cm = CoffeeMachine()

    loop = True

    while loop:
        cmd = input('What would you like? (espresso/latte/cappuccino) :')

        if cmd == "off":
            loop = False
            break
        elif cmd == 'report':
            print(cm.getResources())
            break
        elif cmd == 'espresso' or cmd == 'cappuccino' or cmd == 'latte':
            possibleAns = cm.canServeCoffe(cmd)
            if possibleAns == True :
                money = getMoney()
                print("got : ", money)
                print(cmd + " cost : ", cm.getPrice((cmd)))
                if money >= cm.getPrice(cmd):
                    print("money back : ", money-cm.getPrice(cmd))
                    print("preparing ...")
                    cm.serveCoffe(cmd)
                    print('resources left : ', cm.getResources())

                else:
                    print(" You don't have enough credits . Try again ...")
            else:
                print("missing resource : ", possibleAns)

        else:
            print('wrong command. try again...')
            





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
