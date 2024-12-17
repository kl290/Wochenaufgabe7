def zahl_eingeben(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben!")


print("Dieser Rechner berechnet die Summe, Differenz, Multiplikation und Division von 2 Zahlen.")

Zahl1 = zahl_eingeben("Gib die erste Zahl ein: ")
Zahl2 = zahl_eingeben("Gib die zweite Zahl ein: ")

print(f"{Zahl1} + {Zahl2} = {Zahl1 + Zahl2}")
print(f"{Zahl1} - {Zahl2} = {Zahl1 - Zahl2}")
print(f"{Zahl1} * {Zahl2} = {Zahl1 * Zahl2}")

if Zahl2 != 0:
    print(f"{Zahl1} / {Zahl2} = {Zahl1 / Zahl2}")
else:
    print("Division durch 0 ist nicht erlaubt!")