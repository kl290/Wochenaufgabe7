print("Durchschnittsberechner")


def eingabe_zahlen():
    while True:
        eingabe = input("Bitte gib die Zahlen ein, getrennt durch Leerzeichen: ").strip()

        if not eingabe:
            print("Es wurden keine Zahlen eingegeben. Bitte versuche es erneut.")
            continue

        try:
            return list(map(float, eingabe.split()))
        except ValueError:
            print("Fehler: Du hast einen Buchstaben oder ungültige Zeichen eingegeben.", end="")
            print(" Bitte gib nur Zahlen ein, getrennt durch Leerzeichen.")


zahlen = eingabe_zahlen()

durchschnitt = sum(zahlen) / len(zahlen)
print(f"Der Durchschnitt der eingegebenen Zahlen ist: {durchschnitt}")
