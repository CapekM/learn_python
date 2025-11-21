dvojice = ('Pat', 'Mat')
print(f"{dvojice = }")

osoby = ('máma', 'teta', 'babička')
for osoba in osoby:
    print(f"{osoba = }")


def podil_a_zbytek(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b

podil, zbytek = podil_a_zbytek(12, 5)
print(f"{podil = }\n{zbytek = }")

couple = podil_a_zbytek(12, 5)
