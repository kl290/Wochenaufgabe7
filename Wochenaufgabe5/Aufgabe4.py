def zahl_eingeben():
    while True:
        try:
            return float(input("Bitte geben Sie eine Zahl ein (Wenn Kommazahl, dann getrennt durch . (2.5): "))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine korrekte Zahl eingeben!")


Zahl = zahl_eingeben()

if Zahl == 0:
    print("Die eingegebene Zahl ist 0!")
elif Zahl > 0:
    print("Die eingegebene Zahl ist positiv!")
else:
    print("Die eingegebene Zahl ist negativ!")
