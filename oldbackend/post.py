import cgi
import sqlite3
from datetime import datetime

form = cgi.FieldStorage()

con = sqlite3.connect('mydatabase.db')
cur = con.cursor()

class Post:
    
    def __init__(self, imptext, comments, institution, ment_rating, resource_rating, date_posted=None):
        self.imptext = imptext
        self.comments = comments
        self.institution = institution.capitalize() # Standardizing institution name
        self.ment_rating = ment_rating
        self.resource_rating = resource_rating
        self.date_posted = date_posted if date_posted else datetime.now().strftime('%Y-%m-%d %H:%M:%S') # If date is not provided, use the current date/time
        try: 
            cur.execute("CREATE TABLE posts (imptext varchar(255), comments varchar(255), institution varchar(255), ment_rating int, resource_rating int, date_posted varchar(255))")
        except sqlite3.OperationalError: 
            print(f"table posts already exists")

    def save_to_database(self):
        try:
            cur.execute("INSERT INTO posts (imptext, comments, institution, ment_rating, resource_rating, date_posted) VALUES (?, ?, ?, ?, ?, ?);", 
                (self.imptext, self.comments, self.institution, self.ment_rating, self.resource_rating, self.date_posted))
            con.commit()
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