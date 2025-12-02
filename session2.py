from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List, Dict, Any


class Session2:
    data_dir = Path(__file__).with_name("data")
    cities_file = data_dir / "cities.csv"

    def greet(self, name, greeting="Hello"):
        print(f"{greeting} {name}")

    def calculate(self, a, b):
        """Return both the sum and product as a tuple."""
        return a + b, a * b

    def welcome(self, name="Guest"):
        print(f"Welcome {name}")

    def square(self, x):
        return x * x

    # --- Data tasks ---
    def load_cities(self, path: Path | None = None) -> List[Dict[str, Any]]:
        """Load city data from CSV and return dicts with int population."""
        csv_path = path or self.cities_file
        if not csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_path}")

        rows: List[Dict[str, Any]] = []
        with csv_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                row["population"] = int(row["population"])
                rows.append(row)
        return rows

    def total_population(self, rows: Iterable[Dict[str, Any]]) -> int:
        return sum(row["population"] for row in rows)

    def average_population(self, rows: Iterable[Dict[str, Any]]) -> float:
        rows = list(rows)
        if not rows:
            raise ValueError("Cannot compute average population of empty data")
        return self.total_population(rows) / len(rows)

    def top_cities(self, rows: Iterable[Dict[str, Any]], n: int = 3) -> List[str]:
        rows = list(rows)
        return [
            row["city"]
            for row in sorted(rows, key=lambda r: r["population"], reverse=True)[:n]
        ]

    def _run_examples(self):
        # Basic greeting examples
        self.greet("Alice", "Hi")
        self.greet("Python learner")

        # Demonstrate multiple return values
        a_example, b_example = 2, 3
        sum_, mul_ = self.calculate(a_example, b_example)
        print("=" * 40)
        print("Example 1: Unpacking multiple return values")
        print(f"Input: a = {a_example}, b = {b_example}")
        print(f"Sum (a + b): {sum_}")
        print(f"Product (a * b): {mul_}")
        print()

        # Using the raw tuple
        result_tuple = self.calculate(4, 5)
        print("Example 2: Using the returned tuple directly")
        print(f"Result as tuple: {result_tuple}")
        print(f"First value (sum): {result_tuple[0]}")
        print(f"Second value (product): {result_tuple[1]}")
        print()

        # More examples
        print("=" * 40)
        print("More examples")
        print("=" * 40)
        for a_val, b_val in [(10, 5), (7, 8), (2.5, 4), (-3, 5)]:
            s, p = self.calculate(a_val, b_val)
            print(f"calculate({a_val}, {b_val}): sum={s}, product={p}")
        print()

        # Square helper
        print(f"square(5) = {self.square(5)}")

        # Welcome demo
        self.welcome()
        self.welcome("Nishith")


if __name__ == "__main__":
    session2 = Session2()
    session2._run_examples()
