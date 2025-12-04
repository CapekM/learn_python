slovnik: dict[str, str] = {'Jablko': 'Apple', 'Knoflík': 'Button', 'Myš': 'Mouse'}

print(f"{slovnik['Jablko'] = }")

slovnik['Pes'] = 'Dog'
print(f"{slovnik = }")
slovnik['Pes'] = 'Power strip'
print(f"{slovnik = }")
del slovnik['Pes']
print(f"{'Myš' in slovnik = }")
print(f"{'Mouse' in slovnik = }")

for klic in slovnik:
    print(f"{klic = }")

for hodnota in slovnik.values():
    print(f"{hodnota = }")

for klic, hodnota in slovnik.items():
    print(f"{klic = }, {hodnota = }")

uzivatel: dict[str, str | int | list] = {'jméno': 'Amálka', 'velikost nohy': 36, 'oblíbená čísla': [5, 27]}
