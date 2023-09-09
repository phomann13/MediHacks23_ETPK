import cgi 
import sqlite3

#make in individual methods
form = cgi.FieldStorage() 

# Connect to an SQLite database (creates or opens the 'mydatabase.db' file)
#Make in individual methods
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
#DON'T FORGET conn.close()!!!


#data1 = form.getvalue('__')
    #data2 = form.getvalue('__')
    #....

class Person:
    tot_user = 0 #keep track of users joined, use to assign an web_id to each user
    
    def __init__(self, username, name):
        self.WEB_ID = Person.tot_user 
        Person.tot_user += Person.tot_user + 1
        
        self.username = username 
        self.name = name
        self.institution = None 
        self.post_dict = {}
       
    
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
    

    
    