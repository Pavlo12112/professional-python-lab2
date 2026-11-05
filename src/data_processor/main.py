"""Application entry point."""

from data_processor.analytics import (
    average_by_group,
    calculate_average,
    calculate_average_values,
    create_band_classifier,
    create_grade_filter,
    create_record,
    find_best_student,
    rank_students,
    run_pipeline,
    sort_by_grade,
)
from data_processor.data import GRADE_BANDS, STUDENTS
from data_processor.decorators import repeat
from data_processor.processors import (
    OPERATION_HISTORY,
    count_students_by_group,
    create_id_index,
    create_surname_index,
    filter_by_group,
    filter_items,
    get_unique_groups,
    group_students,
    search_by_name,
)


def print_students(title: str, items: list[dict]) -> None:
    """Print students as a table."""
    print(f"\n{title}")
    print("-" * 52)

    for student in items:
        print(
            f"{student['id']:3} "
            f"{student['name']:20} "
            f"{student['group']:9} "
            f"{student['grade']:6.2f}"
        )


@repeat(2)
def show_message(text: str) -> None:
    """Demonstration of a parametrized decorator."""
    print(text)


def main() -> None:
    students = STUDENTS

    print_students("All students", students)

    print("\nUnique groups:", sorted(get_unique_groups(students)))

    average = calculate_average(students)
    print(f"Average grade: {average:.2f}")

    best = find_best_student(students)
    if best:
        print("Best student:", best["name"], best["grade"])

    print("\nRanking (place, name, grade):")
    for place, name, grade in rank_students(students)[:5]:
        print(f"{place:3} {name:20} {grade:6.2f}")

    print("\nStudents by group:")
    for group, count in sorted(count_students_by_group(students).items()):
        print(f"  {group}: {count}")

    grouped = group_students(students)
    print("\nAverage grade by group:")
    for group, value in sorted(average_by_group(grouped).items()):
        print(f"  {group}: {value:.2f}")

    print_students("Group FeP-33s", filter_by_group(students, "FeP-33s"))

    id_index = create_id_index(students)
    print("\nSearch by id 4:", id_index.get(4))

    surname_index = create_surname_index(students)
    print("Search by surname 'moroz':", surname_index.get("moroz"))
    print("Search by name part 'ko':", [s["name"] for s in search_by_name(students, "ko")])

    is_successful = create_grade_filter(85)
    print_students("Grade >= 85 (closure)", filter_items(students, is_successful))

    print_students(
        "Grade >= 90 (lambda)",
        filter_items(students, lambda student: student["grade"] >= 90),
    )

    classify = create_band_classifier(GRADE_BANDS)
    print("\nBands (closure over tuple of bands):")
    for student in sort_by_grade(students)[:4]:
        print(f"  {student['name']:20} {classify(student)}")

    pipeline_result = run_pipeline(
        students,
        lambda items: filter_items(items, create_grade_filter(70)),
        lambda items: sort_by_grade(items, reverse=False),
        lambda items: items[:3],
    )
    print_students("Pipeline: grade >= 70, ascending, first 3", pipeline_result)

    print("\nAverage via *args:", calculate_average_values(75, 80, 92, 96))

    new_student = create_record(id=11, name="Taras Novak", group="FeP-31", grade=89.0)
    print("Created via **kwargs:", new_student)

    print()
    show_message("Processing...")

    print("\nLast operations (deque):", list(OPERATION_HISTORY))


if __name__ == "__main__":
    main()
