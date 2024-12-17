def punkt_eingabe():
    while True:
        try:
            zahl = int(input("Geben Sie eine Punktezahl zwischen 0 und 100 ein: "))
            if 0 <= zahl <= 100:
                return zahl
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")


punkte = punkt_eingabe()

n = "Die Note lautet:"

if punkte >= 90:
    print(f"{n} Sehr gut")
elif punkte >= 80:
    print(f"{n} Gut")
elif punkte >= 70:
    print(f"{n} Befriedigend")
elif punkte >= 60:
    print(f"{n} Ausreichend")
else:
    print(f"{n} Nicht bestanden")