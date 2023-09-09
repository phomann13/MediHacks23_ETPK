import os
import mysql.connector 
import cgi 



DB_HOST = os.environ.get('DB_HOST', 'localhost')  # Defaults to 'localhost' if not found
DB_USER = os.environ.get('DB_USER', 'root')  # Defaults to 'root' if not found
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')  # Defaults to an empty string if not found
DB_NAME = os.environ.get('DB_NAME', 'medihacks23')  # Defaults to 'medihacks23' if not found

#make in individual methods
form = cgi.FieldStorage() 


class Person:
    tot_user = 0 #keep track of users joined, use to assign an web_id to each user
    
    def __init__(self, username, name):
        self.WEB_ID = Person.tot_user 
        Person.tot_user += 1
        
        self.username = username 
        self.name = name
        self.institution = None 
        self.post_dict = {}
        
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
            
    
    def change_name(self, new_name):
        self.name = new_name
        
    def get_name(self):
        return self.name
        
    def change_username(self, new_username):
        self.username = new_username 
    
    def get_username(self):
        return self.username 
    
    def get_WEB_ID(self):
       return self.WEB_ID 
   
    def get_post(self, title):
        return self.post_dict[title]
    
    def post(self, __):
        #make post (fill out form)
        #add post to self.post_dict 
    

    
    