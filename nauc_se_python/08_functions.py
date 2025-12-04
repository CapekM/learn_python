def zamen(slovo: str, pozice: int, novy_znak: str) -> str:
    """V daném slově zamění znak na dané pozici za daný nový znak."""
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo


print(zamen('kočka', 1, 'a'))
print(zamen('kačka', 2, 'p'))


def napis_hlasku(nazev, skore):
    """Popíše skóre. Název má být přivlastňovací přídavné jméno."""

    print(nazev, 'skóre je', skore)
    if skore > 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště.')


navratova_promenna = napis_hlasku("X", 1)
print(f"{navratova_promenna = }")
print(f"{navratova_promenna=}")
