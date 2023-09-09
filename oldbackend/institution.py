#This is the Institution Class, where the user can choose their insituition (educational),
#And rate their mental health experience from 1-10

class Institution:

    def __init__(self, name):
        self.name = name
        self.students = {}  # Using a dictionary to store students


    def add_student(self, student):
        """Add a student to this institution."""
        if isinstance(student, Person):
            self.students[student.WEB_ID] = student  # Add student to dictionary using their WEB_ID
            student.institution = self.name

    def get_student(self, student_id):
        """Retrieve a student using their WEB_ID."""
        return self.students.get(student_id, None)

    def average_rating(self):
        """Calculate the average rating for this institution."""
        total_rating = 0
        count = 0
        for student in self.students.values():
            for post in student.post_dict.values():
                total_rating += post['rating']
                count += 1
        return total_rating / count if count != 0 else 0

    