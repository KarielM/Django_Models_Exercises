from django.db import models
from datetime import datetime

# Create your models here.
class Airline(models.Model):
    date = models.DateField()
    destination = models.TextField()
    passenger = models.TextField()
    bags = models.IntegerField(default = 0)
    firstclass = models.BooleanField(default = False)


def create_ticket(date, destination, passenger, bags=0, firstclass = False):
    return Airline.objects.create(date = date, destination = destination, passenger = passenger, bags = bags, firstclass = firstclass)

def find_ticket(id):
    try:
         return Airline.objects.get(id = id)
    except:
        raise ValueError
    
def upgrade_firstclass(id):
    if Airline.objects.get(id = id).firstclass == False:
    # if not Airline.objects.get(id = id).firstclass:
        ticket = Airline.objects.get(id = id)
        ticket.firstclass = True
        ticket.save()
        return ticket
    else:
        raise ValueError
    
def delete_ticket(id):
    return Airline.objects.get(id = id).delete()

def all_tickets():
    return Airline.objects.all()

def filter_by_destination(destination):
    return Airline.objects.filter(destination = destination)

def filter_by_firstclass():
    return Airline.objects.filter(firstclass = True)

def update_bags(id, bags):
    ticket = Airline.objects.get(id = id)
    ticket.bags = bags
    ticket.save()
    return ticket