"""Analytics: aggregation, sorting, ranking and higher-order helpers."""

from collections.abc import Callable
from typing import Any

from data_processor.decorators import measure_time


@measure_time
def calculate_average(students: list[dict]) -> float:
    """Average grade (generator expression, no intermediate list)."""
    if not students:
        return 0.0

    return sum(s["grade"] for s in students) / len(students)


def find_best_student(students: list[dict]) -> dict | None:
    """Student with the highest grade."""
    if not students:
        return None

    return max(students, key=lambda student: student["grade"])


def sort_by_grade(students: list[dict], reverse: bool = True) -> list[dict]:
    """Sort students by grade, complexity O(n log n)."""
    return sorted(students, key=lambda student: student["grade"], reverse=reverse)


def rank_students(students: list[dict]) -> list[tuple[int, str, float]]:
    """Ranking: list of tuples (place, name, grade)."""
    ordered = sort_by_grade(students)
    return [(place, s["name"], s["grade"]) for place, s in enumerate(ordered, 1)]


def average_by_group(groups: dict[str, list[dict]]) -> dict[str, float]:
    """Average grade of every group."""
    return {
        group: sum(s["grade"] for s in members) / len(members)
        for group, members in groups.items()
    }


def calculate_average_values(*values: float) -> float:
    """Average of any number of positional arguments (*args)."""
    if not values:
        return 0.0

    return sum(values) / len(values)


def create_record(**fields: Any) -> dict:
    """Create a record from any keyword arguments (**kwargs)."""
    return dict(fields)


def create_grade_filter(minimum_grade: float) -> Callable[[dict], bool]:
    """Closure: predicate remembers ``minimum_grade``."""

    def predicate(student: dict) -> bool:
        return student["grade"] >= minimum_grade

    return predicate


def create_band_classifier(
    bands: tuple[tuple[str, float], ...],
) -> Callable[[dict], str]:
    """Closure: classifier remembers the scale of grade bands."""

    def classify(student: dict) -> str:
        for label, minimum in bands:
            if student["grade"] >= minimum:
                return label
        return bands[-1][0]

    return classify


def run_pipeline(items: list[dict], *steps: Callable[[list[dict]], list[dict]]) -> list[dict]:
    """Pipeline processing: apply steps one after another."""
    result = items

    for step in steps:
        result = step(result)

    return result
