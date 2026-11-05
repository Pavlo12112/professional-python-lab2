"""Unit tests for data_processor."""

import unittest
from collections import Counter

from data_processor.analytics import (
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
from data_processor.processors import (
    count_students_by_group,
    create_id_index,
    filter_by_group,
    filter_items,
    find_linear,
    get_unique_groups,
    group_students,
)


class ProcessorsTest(unittest.TestCase):
    def test_unique_groups(self) -> None:
        self.assertEqual(get_unique_groups(STUDENTS), {"FeP-31", "FeP-32", "FeP-33s"})

    def test_counter_and_group(self) -> None:
        self.assertEqual(
            count_students_by_group(STUDENTS),
            Counter({"FeP-33s": 4, "FeP-31": 3, "FeP-32": 3}),
        )
        grouped = group_students(STUDENTS)
        self.assertEqual(len(grouped["FeP-31"]), 3)
        self.assertEqual(len(filter_by_group(STUDENTS, "FeP-32")), 3)

    def test_index_and_linear_search_agree(self) -> None:
        index = create_id_index(STUDENTS)
        self.assertIs(index[4], find_linear(STUDENTS, 4))
        self.assertIsNone(find_linear(STUDENTS, 999))

    def test_best_and_sort(self) -> None:
        self.assertEqual(find_best_student(STUDENTS)["id"], 4)
        self.assertIsNone(find_best_student([]))
        self.assertEqual(sort_by_grade(STUDENTS)[0]["id"], 4)
        self.assertEqual(rank_students(STUDENTS)[0][0], 1)


class FunctionalTest(unittest.TestCase):
    def test_closure_filter(self) -> None:
        is_good = create_grade_filter(90)
        self.assertEqual({s["id"] for s in filter_items(STUDENTS, is_good)}, {1, 4, 8})

    def test_band_classifier(self) -> None:
        classify = create_band_classifier(GRADE_BANDS)
        self.assertEqual(classify({"grade": 95}), "excellent")
        self.assertEqual(classify({"grade": 50}), "unsatisfactory")

    def test_args_kwargs(self) -> None:
        self.assertEqual(calculate_average_values(10, 20, 30), 20)
        self.assertEqual(calculate_average_values(), 0.0)
        self.assertEqual(create_record(a=1, b=2), {"a": 1, "b": 2})

    def test_pipeline(self) -> None:
        result = run_pipeline(
            STUDENTS,
            lambda items: filter_items(items, create_grade_filter(90)),
            lambda items: sort_by_grade(items),
        )
        self.assertEqual([s["id"] for s in result], [4, 1, 8])


if __name__ == "__main__":
    unittest.main()
