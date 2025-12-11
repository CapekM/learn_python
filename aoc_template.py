from pathlib import Path


def parse(file_data: str) -> list:
    """Parse input."""
    return file_data.split("\n")  # note: you might want to change this


def part1(file_data: str) -> int:
    """Solve part 1."""
    result = 0
    input = parse(file_data)
    # TODO your code here
    return result


def part2(file_data: str) -> int:
    """Solve part 2."""
    result = 0
    input = parse(file_data)
    # TODO your code here
    return result


if __name__ == "__main__":
    PUZZLE_DIR = Path(__file__).parent

    puzzle_input = Path(PUZZLE_DIR / "example.txt").read_text().strip()
    print(f"test: {part1(puzzle_input)}")

    puzzle_input = Path(PUZZLE_DIR / "input.txt").read_text().strip()
    print(f"part1: {part1(puzzle_input)}")

    puzzle_input = Path(PUZZLE_DIR / "input.txt").read_text().strip()
    print(f"part2: {part2(puzzle_input)}")
