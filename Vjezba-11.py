import random

#tb je truebroj

tb = random.randint(1,10)

while True:
    #p je pogodi
    p = int(input("Pogodi broj izmedu 1 i 30:"))

    if p == tb:
        print("Bravo pogodio si trazeni broj")
        break
    else:
        print("Pogrjesio si probaj ponovo !!!")