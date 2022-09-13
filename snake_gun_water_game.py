t="WELCOME TO SNAKE WATER GUN GAME"
print(t.center(155))
a=input("Enter your name:")
z=int(input("How many Round do You want to Play"))
import random
UP=0
CP=0
TP=0
i=0
list=["s","g","w"]
while (i<z):
    print("USER ENTER YOUR CHOICE")
    i+=1
    UC=input()
    UC.lower()
    CC=random.choice(list)
    print(CC)
    def ab():
        h = "*****Score Board*****"
        print(h.center(155))
        print("You:", UP, "COMPUTER:", CP, "TIE:", TP)
    if (UC == "s" and CC == "w") or (UC == "S" and CC == "w"):
        print("Snack drink the water")
        UP += 1
        ab()
    else:
        if (UC == "g" and CC == "s") or (UC == "G" and CC == "s"):
            print("Gun Shoot the Snake")
            UP += 1
            ab()
        else:
            if (UC == "w" and CC == "g") or (UC == "W" and CC == "g"):
                print("Gun Drowning in Water")
                UP += 1
                ab()
            else:
                if (UC == "S" and CC == "s") or (UC == "G" and CC == "g") or (UC == "W" and CC == "w") or (
                        UC == "s" and CC == "s") or (UC == "g" and CC == "g") or (UC == "w" and CC == "w"):
                    print("Tie you both entered same")
                    TP += 1
                    ab()
                else:
                    if (UC == "w" and CC == "s") or (UC == "W" and CC == "s"):
                        print("Snack drink the water")
                        CP += 1
                        ab()
                    else:
                        if (UC == "s" and CC == "g") or (UC == "S" and CC == "g"):
                            print("Gun Shoot the Snake")
                            CP += 1
                            ab()
                        else:
                            if (UC == "g" and CC == "w") or (UC == "G" and CC == "w"):
                                print("Gun Drowning in Water")
                                CP += 1
                                ab()
                            else:
                                print("Enter a Right Input")
                                z=z+1
ab()
if UP>CP:
    print("Congratulation")
    print("You Win the Game with",UP,"-",CP)
    for i in range(10):
        print(" \U0001F973  ")
else:
    if UP==CP:
        print("Match tie")
    else:
     print("Computer Win the Game with",CP,"-",UP)
     print("Better try next time")




