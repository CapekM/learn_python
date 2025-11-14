a = [1, 2, 3]  # Vytvoření seznamu
b = a.copy()  # nebo list(a)

# seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b",
# ale stále pracuješ jenom s jedním seznamem

# Takhle bychom vytvorili kopii a ne pouze odkaz
# b = a.copy()
# b = list(a)

print(f"{id(a) = }")
print(f"{id(b) = }")

print(b)
a.append(4)
print(b)
