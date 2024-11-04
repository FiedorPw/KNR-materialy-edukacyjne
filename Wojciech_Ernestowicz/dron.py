class dron:
    def PlanowanieLotu(dystans):
        for x in range (0, dystans+1):
            if x%3 == 0:
                print(f"{x}/{dystans}", "light")
            elif x%5 == 0:
                print(f"{x}/{dystans}", "drop")
            else: 
                print(f"{x}/{dystans}")


#dron.PlanowanieLotu(200)


def lot(metry):
    for i in range (0, metry):
        if i % 5 == 0:
            print(f"{i}/{metry}", "-> zrzut")
        elif i % 3 == 0:
            print(f"{i}/{metry}", "-> swiatlo")
        else:
            print(f"{i}/{metry}")

lot(100)
