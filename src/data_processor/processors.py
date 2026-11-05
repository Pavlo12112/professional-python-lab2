"""Basic processing of collections: filter, search, group, count."""

from collections import Counter, defaultdict, deque
from collections.abc import Callable

from data_processor.decorators import record_history

# deque with limited size: history of the last operations
OPERATION_HISTORY: deque[str] = deque(maxlen=5)


def get_unique_groups(students: list[dict]) -> set[str]:
    """Set comprehension: unique groups."""
    return {student["group"] for student in students}


def create_id_index(students: list[dict]) -> dict[int, dict]:
    """Dict comprehension: index of students by id."""
    return {student["id"]: student for student in students}


def create_surname_index(students: list[dict]) -> dict[str, dict]:
    """Dict comprehension: index of students by surname (lower case)."""
    return {
        student["name"].split()[-1].lower(): student for student in students
    }


@record_history(OPERATION_HISTORY)
def filter_items(
    items: list[dict], predicate: Callable[[dict], bool]
) -> list[dict]:
    """Universal filter: keep items for which predicate is true."""
    return [item for item in items if predicate(item)]


@record_history(OPERATION_HISTORY)
def filter_by_group(students: list[dict], group: str) -> list[dict]:
    """List comprehension: students of one group."""
    return [student for student in students if student["group"] == group]


@record_history(OPERATION_HISTORY)
def group_students(students: list[dict]) -> dict[str, list[dict]]:
    """Group students by group name using defaultdict."""
    result: defaultdict[str, list[dict]] = defaultdict(list)

    for student in students:
        result[student["group"]].append(student)

    return dict(result)


@record_history(OPERATION_HISTORY)
def count_students_by_group(students: list[dict]) -> Counter:
    """Count students in every group using Counter."""
    return Counter(student["group"] for student in students)


def find_linear(students: list[dict], student_id: int) -> dict | None:
    """Linear search by id, complexity O(n)."""
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def search_by_name(students: list[dict], part: str) -> list[dict]:
    """Search students whose name contains the given text."""
    needle = part.lower()
    return [s for s in students if needle in s["name"].lower()]
