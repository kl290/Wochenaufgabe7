def eingabe_zahl(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine gültige Eingabe tätigen!")