"""Benchmark: search by id in list (O(n)) versus dict index (O(1))."""

from random import Random
from time import perf_counter

from data_processor.processors import create_id_index, find_linear

SIZES: tuple[int, ...] = (1_000, 10_000, 100_000)
LOOKUPS: int = 100


def generate_students(count: int) -> list[dict]:
    """Generate ``count`` synthetic student records."""
    rng = Random(42)
    return [
        {
            "id": number,
            "name": f"Student {number}",
            "group": f"G-{number % 20}",
            "grade": round(rng.uniform(50, 100), 1),
        }
        for number in range(1, count + 1)
    ]


def measure(count: int) -> tuple[float, float, float]:
    """Return times (ms): list search, dict build, dict search.

    The list search looks for the last id (the worst case), LOOKUPS times.
    """
    students = generate_students(count)
    target = count

    start = perf_counter()
    for _ in range(LOOKUPS):
        find_linear(students, target)
    list_ms = (perf_counter() - start) * 1000

    start = perf_counter()
    index = create_id_index(students)
    build_ms = (perf_counter() - start) * 1000

    start = perf_counter()
    for _ in range(LOOKUPS):
        index.get(target)
    dict_ms = (perf_counter() - start) * 1000

    return list_ms, build_ms, dict_ms


def main() -> None:
    print(f"Search of the last id, {LOOKUPS} lookups (time in ms)")
    print(f"{'records':>9}{'list search':>14}{'dict build':>13}{'dict search':>14}")

    for size in SIZES:
        list_ms, build_ms, dict_ms = measure(size)
        print(f"{size:>9}{list_ms:>14.3f}{build_ms:>13.3f}{dict_ms:>14.4f}")


if __name__ == "__main__":
    main()
