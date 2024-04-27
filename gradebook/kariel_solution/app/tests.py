from django.test import TestCase
from app import models
from datetime import datetime

# Create your tests here.
class Test_Gradebook(TestCase):
    # def test_create_grade(self):
    #     grade = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')

    #     self.assertEqual(grade.assignment_name,'exam')
    #     self.assertEqual(grade.percentage,30)
    #     self.assertEqual(grade.student_name,'exame')
    #     self.assertEqual(grade.date,'2024-05-10')
    #     self.assertEqual(grade.notes,'final exam')

    # def test_find_by_id(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     grade = models.find_grade(2)
    #     self.assertEqual(grade, grade2)
    #     self.assertNotEqual(grade, grade1)
    #     self.assertNotEqual(grade, grade3)

    # def test_upgrade_percentage_valid_number(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     grade = models.update_percentage(2, 90)
    #     self.assertEqual(grade.percentage, 90)

    # def test_upgrade_percentage_invalid_number_1(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     with self.assertRaises(ValueError):
    #         models.update_percentage(2, -5)

    # def test_upgrade_percentage_invalid_number_2(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     with self.assertRaises(ValueError):
    #         models.update_percentage(2, 110)

    # def test_update_notes(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     self.assertEqual(grade2.notes, 'final exam')
    #     new_grade2 = models.update_notes(2, 'Midterm Exam')
    #     self.assertEqual(new_grade2.notes, 'Midterm Exam')

    # def test_update_notes_2(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     with self.assertRaises(ValueError):
    #         models.update_notes(4, 'any')

    # def test_delete_grade(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     gradebook1 = models.all_grades()
    #     self.assertEqual(len(gradebook1), 3)
    #     models.delete_grade(2)
        
    #     gradebook2 = models.all_grades()
    #     self.assertEqual(len(gradebook2), 2)

    #     self.assertNotEqual(len(gradebook1), len(gradebook2))

    # def test_delete_grade(self):
    #     grade1 = models.create_grade('exam', 30, 'exame', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'exame', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'exame', '2024-05-10', 'final exam')

    #     with self.assertRaises(ValueError):
    #         models.delete_grade(4)

    # def test_filter_by_name(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     gradebook = models.filter_grades('Ariel')
    #     self.assertEqual(len(gradebook), 2)

    # def test_filter_by_name_2(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam2', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     gradebook = models.filter_grades('Jessica')
    #     self.assertEqual(len(gradebook), 0)

    # def test_filter_by_assignment(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     gradebook = models.filter_assignments('exam')
    #     self.assertEqual(len(gradebook), 2)

    #     gradebook2 = models.filter_assignments('exam3')
    #     self.assertEqual(len(gradebook2), 1)

    # def test_filter_assignments_greaterthan(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam', 90, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade4 = models.create_grade('exam', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade5 = models.create_grade('exam', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade6 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     gradebook = models.filter_grades_greaterthan('exam', 90)
    #     self.assertEqual(len(gradebook), 2)

    #     gradebook2 = models.filter_grades_greaterthan('exam3', 90)
    #     self.assertEqual(len(gradebook2), 1)

    #     gradebook3 = models.filter_grades_greaterthan('exam', 30)
    #     self.assertEqual(len(gradebook3), 4)

    # def test_filter_assignments_greaterthan_2(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam', 90, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade4 = models.create_grade('exam', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade5 = models.create_grade('exam', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade6 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     with self.assertRaises(ValueError):
    #         models.filter_grades_greaterthan('exam', 110)

    # def test_filter_assignments_greaterthan_3(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam', 90, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade4 = models.create_grade('exam', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade5 = models.create_grade('exam', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade6 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     with self.assertRaises(ValueError):
    #         models.filter_grades_greaterthan('exam', -50)

    # def test_filter_assignments_greaterthan_4(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam', 90, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade4 = models.create_grade('exam', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade5 = models.create_grade('exam', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade6 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     gradebook = models.filter_grades_greaterthan('exam2', 50)
    #     self.assertEqual(len(gradebook), 0)

    # def test_filter_assignments_greaterthan_5(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam', 90, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade4 = models.create_grade('exam', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade5 = models.create_grade('exam', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade6 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     gradebook = models.filter_grades_greaterthan('exam', 95)
    #     self.assertEqual(len(gradebook), 0)

    # def test_create_invalid_date(self):
    #     with self.assertRaises(ValueError):
    #         models.create_grade('exam', 30, 'exame', '2024-14-10', 'final exam')

    # def test_create_no_notes(self):
    #     grade = models.create_grade('exam', 30, 'exame', '2024-05-10')

    #     self.assertEqual(grade.assignment_name,'exam')
    #     self.assertEqual(grade.percentage,30)
    #     self.assertEqual(grade.student_name,'exame')
    #     self.assertEqual(grade.date,'2024-05-10')
    #     self.assertIsNone(grade.notes)

    # def test_view_all_grades(self):
    #     grade1 = models.create_grade('exam', 30, 'Ariel', '2024-05-10', 'final exam')
    #     grade2 = models.create_grade('exam', 90, 'Kariel', '2024-05-10', 'final exam')
    #     grade3 = models.create_grade('exam3', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade4 = models.create_grade('exam', 90, 'Ariel', '2024-05-10', 'final exam')
    #     grade5 = models.create_grade('exam', 30, 'Kariel', '2024-05-10', 'final exam')
    #     grade6 = models.create_grade('exam3', 30, 'Ariel', '2024-05-10', 'final exam')

    #     gradebook = models.all_grades()
    #     self.assertEqual(len(gradebook), 6)

    def test_update_date(self):
        grade1 = models.create_grade('exam', 30, 'Ariel')

        self.assertEqual(grade1.date, None)

    def test_update_date_2(self):
        grade1 = models.create_grade('exam', 30, 'Ariel')

        new_grade = models.update_date(1)

        self.assertEqual(new_grade.date, datetime.now().strftime('%Y-%m-%d'))

    def test_update_date_3(self):
        grade1 = models.create_grade('exam', 30, 'Ariel')

        new_grade = models.update_date(1)

        self.assertEqual(new_grade.date, '2024-04-21')