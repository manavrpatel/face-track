from flask_wtf import FlaskForm
from project.model import Allclasses, Student
from wtforms import StringField, SubmitField, FileField, IntegerField
from wtforms.validators import Length, DataRequired, ValidationError


#add new class
class addclassform(FlaskForm):
    def validate_class_name(self, class_to_check):
        classes = Allclasses.query.filter_by(class_name=class_to_check.data).first()
        if classes:
            raise ValidationError('class with same name already exits! Please try Different name')

    class_name = StringField(label='Class Name', validators=[Length(min=4, max=30), DataRequired()])
    class_subject = StringField(label='Subject', validators=[Length(min=4, max=30), DataRequired()])
    submit = SubmitField(label='create Class')


#Add new Student
class addstudentform(FlaskForm):
    def validate_std_rollno(self, std_to_check):
        students = Student.query.filter_by(std_rollno=std_to_check.data).first()
        if students:
            raise ValidationError('Student with same Roll Number already exits! Please try Different Roll no.')

    std_name = StringField(label='Student Name', validators=[Length(min=2, max=30), DataRequired()])
    std_rollno = StringField(label='Student Rollno.', validators=[Length(min=2, max=30), DataRequired()])
    submit = SubmitField(label='create Student')
