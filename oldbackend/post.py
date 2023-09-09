import cgi
import sqlite3
from datetime import datetime

form = cgi.FieldStorage()

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

class Post:
    
    def __init__(self, imptext, comments, institution, ment_rating, resource_rating, date_posted=None):
        self.imptext = imptext
        self.comments = comments
        self.institution = institution.capitalize() # Standardizing institution name
        self.ment_rating = ment_rating
        self.resource_rating = resource_rating
        self.date_posted = date_posted if date_posted else datetime.now() # If date is not provided, use the current date/time

    def save_to_database(self):
        try:
            cursor.execute("INSERT INTO posts (imptext, comments, institution, ment_rating, resource_rating, date_posted) VALUES (?, ?, ?, ?, ?, ?);", 
                (self.imptext, self.comments, self.institution, self.ment_rating, self.resource_rating, self.date_posted))
            conn.commit()
        except Exception as e:
            print(f"Error saving post to database: {e}")

    def get_imptext(self):
        return self.imptext

    def get_comments(self):
        return self.comments
    
    def get_institution(self):
        return self.institution
    
    def date_of_post(self):
        return self.date_posted
    
    def ment_rating(self):
        return self.ment_rating
    
    def resource_rating(self):
        return self.resource_rating