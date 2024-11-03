# Linux

Logowanie do serwera

Powershell w windowsie:

User@(at) IP	

```powershell
ssh KNR@192.168.77.184
```

Podstawowe komendy w linuksie:

```bash
# Listowanie plików i folderów w obecnym katalogu
ls

# Zmienianie katalogu
cd

# Pobieranie informacji o aktualnej lokalizacji katalogu (gdzie się znajdujemy)
pwd

# Tworzenie nowego katalogu
mkdir nowy_katalog

# Usuwanie pliku lub katalogu
# UWAGA: rm -r jest nieodwracalne dla katalogów i plików
rm nazwa_pliku  # dla plików
rm -r nazwa_katalogu  # dla katalogów

# Otworzenie pliku w edytorze tekstu nano
nano

# manager procesów w linuksie
htop

# informacje o systemie
neofetch

#instalowanie pakietów
sudo apt install neofetch
```

# Python

```bash
# Uruchomienie programu Python
python3 nazwa_pliku.py

```

Składnia pythona:

```python
print("Hello, world!")

x = 5       # liczba całkowita
y = 3.14    # liczba zmiennoprzecinkowa
name = "Alice"  # string
is_student = True  # wartość logiczna (boolean)

print(x, y, name, is_student, "tak możemy printować zmienne i tekst")

# Pętla for
for fruit in fruits:
    print("Owoc:", fruit)

# Pętla while
counter = 0
while counter < 3:
    print("Licznik:", counter)
    counter += 1

# Funkcje - Definiowanie i wywoływanie funkcji
def greet(name):
    print("Hello,", name)

greet("Alice")

# Praca z listami (tablice)
fruits = ["apple", "banana", "cherry"]

# dodawanie elementu
fruits.append("orange")  

# usuwanie elementu
fruits.remove("banana")  

# dostęp do elementu przez indeks
print("Pierwszy owoc:", fruits[0])  

# Klasy i obiekty - podstawy programowania obiektowego
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

student1 = Student("Alice", 21)
student1.introduce()

```

# Git

```bash
# Klonowanie repozytorium Git
git clone <URL_repozytorium>

# Updateowanie repozytorium(robimy to przed każdym pushem)
git pull

# Dodawanie plików do commita
git add .

# Tworzenie commita
git commit -m "Komunikat commita"

# Wysyłanie zmian na zdalne repozytorium
git push origin main

# Sprawdzanie wersji Git
git --version

```
