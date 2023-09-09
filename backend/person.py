class Person:
    import #the file with the form info
    form = #the file with the form info.FieldStorage()
    #data1 = form.getvalue('__')
    #data2 = form.getvalue('__')
    #....
    
    def __init__(self, name, uid, day, month, year):
        self.uid = uid 
        self.name = name
        self.age_array = []
        
        self.age_array.append(day)
        self.age_array.append(month)
        self.age_array.append(year)

    def change_uid(self, new_uid):
        self.uid = new_uid
    
    def change_name(self, new_name):
        self.name = new_name
    
    def change_age(self, day, month, year):
        self.age_array[0] = day
        self.age_array[1] = month
        self.age_array[2] = year
    
    def post(): #tbd 
    
    
    