import os
import sqlite3
import cgi 

#connecting to sqlite3 database
con = sqlite3.connect("medihacks.db")
cur = con.cursor()

#make in individual methods
form = cgi.FieldStorage() 
username = form.getvalue('username')
password = form.getvalue('password')

class Person:

    tot_user = 0 #keep track of users joined, use to assign an web_id to each user
    
    def __init__(self, username, name, password):
        Person.tot_user += 1
        
        self.username = username 
        self.name = name
        self.institution = None 
        self.post_dict = {}
        self.password = password
        self.logged_in = False
        
        try: 
            #creating table for students
            cur.execute("CREATE TABLE students (WEB_ID int, username varchar(255), name varchar(255), institution varchar(255))")
        except sqlite3.OperationalError: 
            #table already exists in the database
            print("students already exists")

        cur.execute("INSERT INTO students (WEB_ID, username, name, institution) VALUES (%s, %s, %s, %s);", 
            (self.WEB_ID, self.username, self.name, self.institution))
            
    def login(self, password):
        # Check the provided password against the user's stored password
        if password == self.password:
            self.logged_in = True
             # Successful login; redirect to a dashboard or another page
            print("Location: dashboard.py")  # Redirect to the dashboard
        else:
            self.logged_in = False
            # Failed login; redirect back to the login page with an error message
            print("Location: login.html?error=1")
    
    def change_name(self, new_name):
        if self.logged_in:
            self.name = new_name
        else:
            return "You must be logged in to change your name."
        
    def get_name(self):
        return self.name
        
    def change_username(self, new_username):
        if self.logged_in:
            self.username = new_username 
        else:
            return "You must be logged in to change your name."
    
    def get_username(self):
        return self.username 
 
    def get_post(self, title):
        return self.post_dict[title]
    
    def post(self, __):
        #make post (fill out form)
        #add post to self.post_dict 
    

    
    