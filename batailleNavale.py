import random

TAILLE = 10
x, y = 0, 0
bateau_x = random.randint(0, 9)
bateau_y = random.randint(0, 9)

while True:

    print("--- BATAILLE NAVALE ---")
    print(f"Position x : {x}, y : {y}")

    print(bateau_x, bateau_y)

    for ligne in range(TAILLE):
        for colonne in range(TAILLE):
            if colonne == y and ligne == x:
                print("T", end=" ")
            else:
                print(".", end=" ")
        print()

    commande = input("Naviguez puis tirer ! (z/s/q/d/t) ")

    if commande == "s" and x < 9:
        x = x + 1
    elif commande == "z" and x > 0:
        x = x - 1 
    elif commande == "q" and y > 0:
        y = y - 1
    elif commande == "d" and y < 9:
        y = y + 1
    elif commande == "t":
        if bateau_x == x and bateau_y == y:
            print("TOUCHER")
            break
        else:
            print("RATÉ")
    
    
