from django.db import models
from datetime import datetime

# Create your models here.
class ExpenseTracker(models.Model):
    Date = models.DateField()
    Location = models.TextField()
    Amount = models.FloatField()
    Notes = models.TextField(null = True)

###these functions are defined OUTSIDE of the class

def create_an_expense(date, location, amount, notes=None):
    return ExpenseTracker.objects.create(Date = date, Location = location, Amount = amount, Notes = notes)

def update_an_expense(id, field, newValue):
    #typo =_=
    ### so i didn't read enough ig. you pull a single one 
    ## based on id and then assign it a new value
    ##not writing tests for this one bc it'll be tedious
    ### been so long since i had to do inputs i forgot
    ## that that's what prompt means

    field_to_update = input('''Which field would you like to update
                            (Date, Location, Amount, Notes)''').lower()
    while field_to_update.lower() not in ['date', 'location', 'amount', 'notes']:
        field_to_update = input('''Which field would you like to update
                            (Date, Location, Amount, Notes)''').lower()
        
    if field_to_update == 'date':
        new_date = input("Enter the new date (YYYY-MM-DD): ")
        try:
            datetime.strptime(new_date, "%m-%d")
            ExpenseTracker["Date"] = new_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    else:
        new_value = input(f"Enter the new value for {field_to_update}: ")
        ExpenseTracker[field_to_update.upper()] = new_value  


def delete_an_expense(id:int):
    ExpenseTracker.objects.get(id = id).delete()

def filter_by_location_and_amount(location, amount):
    try:
        return ExpenseTracker.objects.filter(Location = location, Amount = amount)
    except:
        pass

def show_all_expenses_report():
    return ExpenseTracker.objects.all()

def return_amount_as_string(id):
    ### all??? or just one????
    ### gonna do just one
    amount = ExpenseTracker.objects.get(id = id)
    return f'${amount.Amount:.2f}'


#####we're going to finish this tomorrow w/ tests, datetime, and that 
### update function