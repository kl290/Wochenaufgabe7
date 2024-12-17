print("Multiplikationstabelle ( kleines 1-mal-1 )")


def zahl_eingeben():
    while True:
        try:
            return int(input("Bitte gib eine Zahl ein: "))
        except ValueError:
            print("Fehler: Bitte gib eine gültige Zahl ein!")


zahl = zahl_eingeben()

for i in range(1, 11):
    print(f"{zahl} * {i} = {zahl * i}")
