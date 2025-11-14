barva_travy: str = 'zelená'
pocet_kotatek: int = 28


def popis_stav() -> str:
    return f'Tráva je {barva_travy}. Prohání se po ní {pocet_kotatek} koťátek'


print('Louka je zelená!')  # vypise se pri prvnim importu
