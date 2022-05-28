from project import db
from project.model import Allclasses, Student
import pickle


#get total students in a class
def total_student():
    total_student=[0]
    rows = Allclasses.query.all()
    for row in rows:
        count = Student.query.filter_by(std_class=row.id).count()
        total_student.append(count)
    return total_student

#get present students in a class
def present_student():
    present_student=[0]
    rows = Allclasses.query.all()
    for row in rows:
        count = Student.query.filter_by(std_class=row.id, std_attendance=1).count()
        present_student.append(count)
    return present_student

#Mark present
def attendance(name, class_id):
    present_student = Student.query.filter_by(std_name=name, std_class=class_id).first()
    present_student.std_attendance = 1
    db.session.commit()
    

#generate face encodings
def get_face_encodings(classid):
    known_face_encodings=[]
    rows = Student.query.with_entities(Student.std_img).filter_by(std_class=classid)
    for each in rows:
        for face_stored_pickled_data in each:
            face_data = pickle.loads(face_stored_pickled_data)
            known_face_encodings.append(face_data)
    return known_face_encodings

#generate face names
def get_face_names(classid):
    known_face_names=[]
    namelist = Student.query.with_entities(Student.std_name).filter_by(std_class=classid)
    for each in namelist:
        for face_names in each:
            known_face_names.append(face_names)
    return known_face_names

