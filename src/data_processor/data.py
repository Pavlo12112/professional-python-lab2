"""Input data of the application."""

# list of dict: one dict is one student record
STUDENTS: list[dict] = [
    {"id": 1, "name": "Pavlo Tsiastun", "group": "FeP-33s", "grade": 93.4},
    {"id": 2, "name": "Olena Savchuk", "group": "FeP-33s", "grade": 87.1},
    {"id": 3, "name": "Taras Hrytsenko", "group": "FeP-31", "grade": 71.8},
    {"id": 4, "name": "Sofiia Lysenko", "group": "FeP-32", "grade": 96.0},
    {"id": 5, "name": "Maksym Kravets", "group": "FeP-31", "grade": 64.5},
    {"id": 6, "name": "Kateryna Moroz", "group": "FeP-33s", "grade": 78.9},
    {"id": 7, "name": "Dmytro Bilyk", "group": "FeP-32", "grade": 82.3},
    {"id": 8, "name": "Yulia Pavlenko", "group": "FeP-31", "grade": 90.2},
    {"id": 9, "name": "Bohdan Rudenko", "group": "FeP-32", "grade": 55.7},
    {"id": 10, "name": "Iryna Kovalenko", "group": "FeP-33s", "grade": 85.6},
]

# tuple of tuples: immutable classification scale (label, minimal grade)
GRADE_BANDS: tuple[tuple[str, float], ...] = (
    ("excellent", 90.0),
    ("good", 75.0),
    ("satisfactory", 60.0),
    ("unsatisfactory", 0.0),
)

# tuple: fixed set of fields of a student record
STUDENT_FIELDS: tuple[str, ...] = ("id", "name", "group", "grade")
