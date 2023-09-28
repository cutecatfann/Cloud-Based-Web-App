"""
Python list model
Name
Description
Street Address
Type of service
Phone number
Hours of Operation
Reviews
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.guestentries = []

    def select(self):
        """
        Returns guestentries list of lists
        Each list in guestentries contains: name, email, date, phone number, description of business
            street address, service type, hours of operation, reviews
        :return: List of lists
        """
        return self.guestentries

    def insert(self, name, email, phone_number, description, street_address, service_type, hours_operation,reviews):
        """
        Appends a new list of values representing new message into guestentries
        :param name: String
        :param email: String
        :param phone_number: string
        :param description: string
        :param street_address: string
        :param service_type: string
        :param hours_operation: string
        param reviews: string

        :return: True
        """
        params = [name, email, phone_number,date.today(),description,street_address,service_type,hours_operation,reviews]
        self.guestentries.append(params)
        return True
