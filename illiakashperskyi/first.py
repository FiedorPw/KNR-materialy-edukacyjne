def zaplanuj_trase (metry):
    
    for i in range(1,metry):
        if i % 3 == 0:
            pass
            print(i, "/", metry, "m", "zrzucamy")
        elif i % 5 == 0:
            pass
            print(i, "/", metry, "m", "swiecimy")
        else:
            print(i, "/", metry, "m")

zaplanuj_trase(100)        
        
            