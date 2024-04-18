from django.test import TestCase
from app import models

class Test_Airline_Model(TestCase):
    def test_view_all_passengers(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Bermuda',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )

        passenger_list = models.all_tickets()

        self.assertEqual(len(passengers), len(passenger_list))

    def test_delete_passenger(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Bermuda',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )

        models.delete_ticket(2)
        passenger_list = models.all_tickets()
        self.assertEqual(len(passenger_list), 2)

    def test_create_new_ticket(self):
        ticket = models.create_ticket('2024-06-10','Jamaica', 'Kariel')
        self.assertEqual(ticket.date, '2024-06-10')
        self.assertEqual(ticket.destination, 'Jamaica')
        self.assertEqual(ticket.passenger, 'Kariel')
        self.assertEqual(ticket.bags, 0)
        self.assertEqual(ticket.firstclass, False)

    def test_create_new_ticket_2(self):
        ticket = models.create_ticket('2024-06-10','Jamaica', 'Kariel', 4, True)
        self.assertEqual(ticket.date, '2024-06-10')
        self.assertEqual(ticket.destination, 'Jamaica')
        self.assertEqual(ticket.passenger, 'Kariel')
        self.assertEqual(ticket.bags, 4)
        self.assertEqual(ticket.firstclass, True)

    def test_find_by_id(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Bermuda',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )

        passenger_list = models.all_tickets()

        ticket = models.find_ticket(2)
        self.assertEqual(passenger_list[1], ticket)

    def test_find_by_id_2(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Bermuda',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )
        
        with self.assertRaises(ValueError):
            models.find_ticket(525600)
    
    def test_upgrade_to_firstclass(self):
        ticket = models.create_ticket('2024-06-10','Jamaica', 'Kariel')
        new_ticket = models.upgrade_firstclass(ticket.id)
        print(ticket.firstclass)
        self.assertTrue(new_ticket.firstclass)

    def test_upgrade_to_firstclass_2(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Bermuda',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )
        
        ticket = models.find_ticket(3)
        models.upgrade_firstclass(ticket.id)
        ticket_list = models.all_tickets()

        self.assertTrue(ticket_list[2].firstclass)

    def test_upgrade_firstclass_3(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': True
            },
            {
                'date': '2024-06-01',
                'destination': 'Bermuda',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )

        with self.assertRaises(ValueError):
            models.upgrade_firstclass(2)

    def test_update_bags(self):
        models.create_ticket('2024-06-10','Jamaica', 'Kariel')
        new_ticket = models.update_bags(1, 5)
        self.assertEqual(new_ticket.bags, 5)

    def test_update_bags_2(self):
        models.create_ticket('2024-06-10','Jamaica', 'Kariel', 5)
        new_ticket = models.update_bags(1, 0)
        self.assertEqual(new_ticket.bags, 0)

    def test_filter_by_first_class(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': True
            },
            {
                'date': '2024-06-01',
                'destination': 'Bermuda',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )

        firstclass_list = models.filter_by_firstclass()
        self.assertEqual(len(firstclass_list), 1)

    def test_filter_by_destination(self):
        passengers = [
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Kariel',
                'bags': 2,
                'firstclass': False
            },
            {
                'date': '2024-06-01',
                'destination': 'Jamaica',
                'passenger': 'Ariel',
                'bags': 2,
                'firstclass': True
            },
            {
                'date': '2024-06-01',
                'destination': 'Aruba',
                'passenger': 'Jessica',
                'bags': 2,
                'firstclass': False
            },
        ]

        for passenger in passengers:
            models.create_ticket(
                passenger['date'],
                passenger['destination'],
                passenger['passenger'],
                passenger['bags'],
                passenger['firstclass']
            )

        destination_list = models.filter_by_destination('Aruba')
        self.assertEqual(len(destination_list), 2)