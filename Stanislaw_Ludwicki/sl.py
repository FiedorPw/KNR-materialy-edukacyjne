def zaplanuj(metry):
    for i in range(1, metry):
        print(i, "/", metry,"m", end="")

        if i%3 == 0 :
            print(" zrzut", end="")
        if i%5==0:
            print(" światło", end="")
        print()

zaplanuj(100)