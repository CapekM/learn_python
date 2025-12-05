class Kotatko:
    def __init__(self, jmeno: str) -> None:
        self.jmeno: str = jmeno

    def __str__(self) -> str:
        return f'<Kotatko jmenem {self.jmeno}>'

    def zamnoukej(self) -> None:
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo: str) -> None:
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")


mourek = Kotatko('Mourek')
# mourek.snez('ryba')
print(mourek)
