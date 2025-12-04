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

# typovani listu a tupelu
list_int: list[int] = [1, 2, 3]
tuple_int: tuple[int, int, int] = (1, 2, 3)
tuple_int_2: tuple[int, ...] = (1, 2, 3)  # nevim velikost podle typu
list_int_str: list[int | str] = [1, "a", 3, "b"]
tuple_int_str: tuple[int, str, int, str] = (1, "a", 3, "b")
tuple_int_str2: tuple[int | str, ...] = (1, "a", 3, "b")  # nevim velikost podle typu
