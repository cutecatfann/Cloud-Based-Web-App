"""
A simple charity flask app

This is created using SQL
Command used: create table guestbook (name text, email text, signed_on date, message);

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
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    """Builds the model for backend. Creates SQL database"""
    
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from charities")
        except sqlite3.OperationalError:
            cursor.execute("create table charities (name text, email text, signed_on date, phone_number text, description text, street_address text, service_type text, hours_operation text, reviews text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, signed_on date, phone_number, description, street_address, 
            service_type,hours_operation, reviews
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM charities")
        return cursor.fetchall()

    def insert(self, name, email, phone_number, description, street_address, service_type,hours_operation, reviews):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param phone_number: string
        :param description: string
        :param street_address: string
        :param service_type: string
        :param hours_operation: string
        param reviews: string
        
        :return: True
        :raises: Database errors on connection and insertion
        """
        
        params = {'name':name, 'email':email,'phone_number':phone_number,'signed_on':date.today(),'description':description, 'street_address':street_address, 'service_type':service_type, 'hours_operation':hours_operation, 'reviews':reviews}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into charities (name, email, phone_number, signed_on, description, street_address, service_type,hours_operation, reviews) VALUES (:name, :email, :phone_number, :signed_on, :description, :street_address, :service_type, :hours_operation, :reviews)", params)

        connection.commit()
        cursor.close()
        return True
