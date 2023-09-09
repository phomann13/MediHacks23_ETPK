import mysql.connector

class Person:
    import #the file with the form info

    form = #the file with the form info.FieldStorage()
    #data1 = form.getvalue('__')
    #data2 = form.getvalue('__')
    #....
    tot_user = 0 #keep track of users joined, use to assign an web_id to each user
    
    def __init__(self, username, name):
        self.WEB_ID = Person.tot_user 
        Person.tot_user += Person.tot_user + 1
        
        self.username = username 
        self.name = name
        self.institution = None 
        self.post_dict = {}
        
        db = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Tomh1015!",
            database="medihacks23"
            )

        cursor = db.cursor()

        cursor.execute("INSERT INTO students VALUES (%i, %s, %s, %s); ", 
                (self.WEB_ID, self.username, self.name, self.institution))
        
    
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
    

    
    