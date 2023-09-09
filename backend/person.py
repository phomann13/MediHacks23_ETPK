import os
import mysql.connector 
import cgi 



DB_HOST = os.environ.get('DB_HOST', 'localhost')  # Defaults to 'localhost' if not found
DB_USER = os.environ.get('DB_USER', 'root')  # Defaults to 'root' if not found
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')  # Defaults to an empty string if not found
DB_NAME = os.environ.get('DB_NAME', 'medihacks23')  # Defaults to 'medihacks23' if not found

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
            db = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                passwd=DB_PASSWORD,
                database=DB_NAME
                )
            
            cursor = db.cursor()

            cursor.execute("INSERT INTO students (WEB_ID, username, name, institution) VALUES (%s, %s, %s, %s);", 
                    (self.WEB_ID, self.username, self.name, self.institution))
            db.commit()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            db.close()
            
    def login(self, password):
        # Check the provided password against the user's stored password
        try:
            db = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                passwd=DB_PASSWORD,
                database=DB_NAME
                )
            
            cursor = db.cursor()

            cursor.execute("INSERT INTO students (WEB_ID, username, name, institution) VALUES (%s, %s, %s, %s);", 
                    (self.WEB_ID, self.username, self.name, self.institution))
            db.commit()

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            db.close()
            
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
        
    def change_username(self, new_username):
        if self.logged_in:
            self.username = new_username 
        else:
            return "You must be logged in to change your name."
    

    
    