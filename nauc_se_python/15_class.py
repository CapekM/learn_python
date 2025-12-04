class Kotatko:
    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")


mourek = Kotatko()  # Vytvoření konkrétního objektu
mourek.jmeno = 'Mourek'

print(mourek.jmeno)
mourek.zamnoukej()  # Volání metody
