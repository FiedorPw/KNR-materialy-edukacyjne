#include <iostream> 

def main():
    i = 1
    while i < 101:
        if i % 3 == 0:
            print(i)
            print ("/100m -> swiatlo")
            if i % 5 == 0:
                print(i)
                print ("/100m -> swiatlo i zrzut")
        else:
            print(i)
            print ("/100m")
        if i % 5 == 0:
            print(i)
            print ("/100m -> zrzut")
        elif i % 3 == 0:
            pass
        i +=1
        
main()