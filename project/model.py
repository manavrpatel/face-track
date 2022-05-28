from project import db


#model for a Class
class Allclasses(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    class_name = db.Column(db.String(length=50), nullable=False, unique=True)
    class_subject = db.Column(db.String(length=50), nullable=False)
    def __repr__(self):
        return f'Allclasses{self.class_name}'

#model for a Student
class Student(db.Model):
    std_id = db.Column(db.Integer(), primary_key=True)
    std_name = db.Column(db.String(length=50), nullable=False)
    std_rollno = db.Column(db.String(length=50), nullable=False, unique=True)
    std_img = db.Column(db.BLOB, nullable=False)
    std_class = db.Column(db.Integer(), nullable=False)
    std_attendance = db.Column(db.Integer(), default=0)
    
    def __repr__(self):
        return f'Student{self.std_name}'