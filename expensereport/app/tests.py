from django.test import TestCase
from app import models

# Create your tests here.
##splitting these up so they aren't too long
#test cases
#i still have to reference other exercises to write the test bc it's a lot
#plus i test the easy ones first/ create/read/delete. 
#all the other ones are the ones that take more to test

class Test_Expense_Tracker(TestCase):
    def test_create_expense(self):
        #this is eh bc irl we'd want to use... input validation
        #to make sure we get the right date format
        expense = models.create_an_expense(
            '2024-06-10',
            'Oxford',
            500,
            'Buy a playstation ig'
        )

        self.assertEqual(expense.Date, '2024-06-10')
        self.assertEqual(expense.Location, 'Oxford')
        self.assertEqual(expense.Amount, 500)
        self.assertEqual(expense.Notes, 'Buy a playstation ig')

##whenever you make changes to your model you run makemigrations
##then migrate
##i forgot to in this video. tests won't run if your 
#migrations aren't up to date
    def test_notes_field_can_be_null(self):
        expense = models.create_an_expense(
            '2024-06-10',
            'Oxford',
            500,
            # self.assertEqual(expense.Notes, None)
        )

        self.assertEqual(expense.Date, '2024-06-10')
        self.assertEqual(expense.Location, 'Oxford')
        self.assertEqual(expense.Amount, 500)
        self.assertIsNone(expense.Notes)
        # self.assertIsNone(expense.Notes) this isn't working bc there's a problem
        # with my function. it needs a notes parameter
        ## DUMB MISTAKE I FORGOT TO SET NOTES AS NONE FOR THE DEFAULT
        #SETTING IT AS THAT MAKES IT SO THEY DON'T HAVE TO PUT IT IN THERE IF THEY DON'T WANT
        #LITERALLY FACEPALM MOMEMT

    def test_read_all_expenses(self):
        expense_report = [
            {'date': '2024-06-10',
            'location': 'Oxford',
            'amount': 500,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-11',
            'location': 'Oxford',
            'amount': 600,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-12',
            'location': 'Oxford',
            'amount': 700,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-13',
            'location': 'Oxford',
            'amount': 800,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-14',
           'location': 'Oxford',
            'amount': 900,
            'notes': 'Buy a playstation ig'},
        ]
        #         for contact_data in contacts_data:
#             models.create_contact(
#                 contact_data["name"],
#                 contact_data["email"],
#                 contact_data["phone"],
#                 contact_data["is_favorite"],
#             )
        for expense in expense_report:
            models.create_an_expense(
                expense['date'],
                expense['location'],
                expense['amount'],
                expense['notes']
            )
        expenses = models.show_all_expenses_report()
        self.assertEqual(len(expenses), len(expense_report))

    def test_delete_an_expense(self):
        expense_report = [
            {'date': '2024-06-10',
            'location': 'Oxford',
            'amount': 500,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-11',
            'location': 'Oxford',
            'amount': 600,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-12',
            'location': 'Oxford',
            'amount': 700,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-13',
            'location': 'Oxford',
            'amount': 800,
            'notes': 'Buy a playstation ig'},
            {'date': '2024-06-14',
           'location': 'Oxford',
            'amount': 900,
            'notes': 'Buy a playstation ig'},
        ]

        for expense in expense_report:
            models.create_an_expense(
                expense['date'],
                expense['location'],
                expense['amount'],
                expense['notes']
            )

        models.delete_an_expense(2)
        #deletes second item in list
        self.assertEqual(len(models.show_all_expenses_report()), 4)
        ##this isn't working bc i forgot to make it a model =_=
        #ugh