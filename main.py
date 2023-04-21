"""
Gra wisielec
"""
print("Witaj w grze wisielec")
haslo = input("Wprowadz haslo do odgadniecia: ")
wyswietlany_napis = "_" * len(haslo)
licznik_zyc = 5


def odswiez_widok(znak):
    global wyswietlany_napis
    nowy_napis = ""
    for i in range(len(haslo)):
        if haslo[i] == znak:
            nowy_napis += znak
        else:
            nowy_napis += wyswietlany_napis[i]
    wyswietlany_napis = nowy_napis

def game():
    global licznik_zyc
    while licznik_zyc > 0:
        if licznik_zyc == 5:
            print("------\n"
                  "|    |\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "------\n"   
                  "")
        if licznik_zyc == 4:
            print("------\n"
                  "|    |\n"
                  "|    0\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "------\n"
                  "")
        if licznik_zyc == 3:
            print("------\n"
                  "|    |\n"
                  "| \  0  /\n"
                  "|  \-=-/\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "|\n"
                  "------\n"
                  "")
        if licznik_zyc == 2:
            print("------\n"
                  "|    |\n"
                  "|    |\n"
                  "| \  0  /\n"
                  "|  \-=-/\n"
                  "|    |\n"
                  "|    |\n"
                  "|\n"
                  "|\n"
                  "------"
                  "")
        if licznik_zyc == 1:
            print("------\n"
                  "|    |\n"
                  "|    |\n"
                  "| \  0  /\n"
                  "|  \-=-/\n"
                  "|    |\n"
                  "|    |\n"
                  "|   / \ \n"
                  "|  /   \ \n"
                  "------"
                  "")
        print(f"Licznik zyc: {licznik_zyc}")
        print(f"{wyswietlany_napis}\n")
        znak = input("Podaj znak: \n")

        if znak in haslo:
            odswiez_widok(znak)
            if wyswietlany_napis == haslo:
                print()
                print(f"Wygrales! Haslo to {haslo}.")
                break
        else:
            licznik_zyc -= 1

    if licznik_zyc == 0:
        print("\nPrzegrales!")


if __name__ == "__main__":
    game()