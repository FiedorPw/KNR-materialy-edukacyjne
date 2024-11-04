import time

def mission_control(metry):
    for n in range(1,metry+1):
        text = f'{n} / {metry}m'
        if n % 5 == 0:
            if n % 3 == 0:
                text += " -> światło i zrzut"
            else:
                text += " -> zrzut"
        elif n % 3 == 0:
            text += " -> światło"
        time.sleep(0.3)
        print(text)
    
print(mission_control(100))   

