def zaplanuj_trase(metry):
    for i in range(1,metry):
        print(i,"/",metry,"m")
        if i%3==0 and i%5==0:
            print("zrzucamy i świecimy")
        elif i%3==0:
            print("świecimy")
        elif i%5==0:
            print("zrzucamy")

    
zaplanuj_trase(100)

    