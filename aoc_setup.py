import argparse
import datetime
import shutil
from pathlib import Path

TEMPLATE_FILE = 'aoc_template.py'  # The file to copy from


def create_structure(year: int, day: int) -> None:
    # 1. Create Directory: YEAR/day (e.g., 2024/05)
    base_dir = Path(str(year))
    day_dir = base_dir / f"{day:02d}"

    # Create the folder
    day_dir.mkdir(parents=True, exist_ok=True)

    # 2. Copy Template -> main.py
    target_main = day_dir / "main.py"
    if not target_main.exists():
        if Path(TEMPLATE_FILE).exists():
            shutil.copy(TEMPLATE_FILE, target_main)
            print(f"  - Copied {TEMPLATE_FILE} to main.py")
        else:
            print(f"  - WARNING: {TEMPLATE_FILE} not found in root. Created empty main.py")
            target_main.touch()
    else:
        print("  - main.py already exists")

    # 3. Create txt files: example.txt, input1.txt, input2.txt
    (day_dir / "example.txt").touch()
    print("  - Created example.txt")

    (day_dir / "input.txt").touch()
    print("  - Created input.txt")


def main():
    parser = argparse.ArgumentParser(description='AoC Custom Setup')
    parser.add_argument('day', type=int, nargs='?', default=datetime.datetime.now().day, help='The day number')
    parser.add_argument('year', type=int, nargs='?', default=datetime.datetime.now().year, help='The year')

    args = parser.parse_args()

    print(f"--- Setting up Day {args.day}, {args.year} ---")
    create_structure(args.year, args.day)
    print("--- Done ---")


if __name__ == "__main__":
    main()
