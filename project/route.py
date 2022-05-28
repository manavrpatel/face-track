from project import app, db
from flask import render_template, redirect, url_for, flash, request, Response

from project.forms import addclassform, addstudentform
from project.model import Allclasses, Student
from project.camcapture import gen_frames
from project.screencapture import gen_shots
from project.function import total_student, present_student, get_face_encodings, get_face_names

import csv
import io

import pickle
import face_recognition


#landing page
@app.route('/')
@app.route('/getstarted')
def get_started():
    return render_template('/landing_page/getstarted.html')

#classrooms
@app.route('/classrooms')
def classrooms_page():
    classes = Allclasses.query.all()
    total_std = total_student()
    present_std = present_student()
    return render_template('classroom.html', classes = classes, total_std=total_std ,present_std=present_std)



#Load people section
@app.route('/<classid>/classinfo_c')
def info_page(classid) :
    class_id = classid
    classinfo = Allclasses.query.filter_by(id=class_id).first()
    people = Student.query.filter_by(std_class=class_id)
    return render_template('switch_to_cam.html',class_id=class_id ,people = people, classinfo = classinfo)

#load people section to mark attendance using screen capture
@app.route('/<classid>/classinfo_s')
def info_page_sc(classid) :
    class_id = classid
    classinfo = Allclasses.query.filter_by(id=class_id).first()
    people = Student.query.filter_by(std_class=class_id)
    return render_template('switch_to_screen.html',class_id=class_id ,people = people, classinfo = classinfo)

#reset attendance
@app.route('/<class_id>/reset')
def reset_attendance(class_id):
    class_id = class_id
    reset_att = Student.query.all()
    for std in reset_att:
        std.std_attendance=0
    db.session.commit()
    return redirect(url_for('info_page', classid=class_id))



#manually mark a student present
@app.route('/<std_id>/present')
def mark_present(std_id):
    std_id = std_id
    student_to_markpresent = Student.query.filter_by(std_id=std_id).first()
    student_to_markpresent.std_attendance = 1
    db.session.commit()
    return redirect(url_for('info_page', classid=student_to_markpresent.std_class))

#manually mark a student absent
@app.route('/<std_id>/absent')
def mark_absent(std_id):
    std_id = std_id
    student_to_markabsent = Student.query.filter_by(std_id=std_id).first()
    student_to_markabsent.std_attendance = 0
    db.session.commit()
    return redirect(url_for('info_page', classid=student_to_markabsent.std_class))



#Add new class
@app.route('/addnewclass', methods=['GET', 'POST'])
def addclass_page():
    form = addclassform()
    if form.validate_on_submit():
        class_to_create = Allclasses(class_name=form.class_name.data, class_subject=form.class_subject.data)
        db.session.add(class_to_create)
        db.session.commit()
        return redirect(url_for('classrooms_page'))

    if form.errors !={} :
        for err_msg in form.errors.values():
            flash(f'There was an error with creating New class:{err_msg}', category='danger')         
    return render_template('/addentity/addclasses.html', form=form)

#Add new Student
@app.route('/<std_class>/addnewstudent', methods=['GET', 'POST'])
def addstudent_page(std_class) :
    std_class = std_class
    form = addstudentform()

    if form.validate_on_submit():
        print(form.std_name.data)
        pic = request.files['pic']
        if not pic:
            return 'No pic uploaded!', 400

        face_image = face_recognition.load_image_file(pic)
        face_encoding = face_recognition.face_encodings(face_image)[0]
        face_pickled_data = pickle.dumps(face_encoding)
        
        std_to_create = Student(std_name=form.std_name.data, std_img=face_pickled_data, std_rollno=form.std_rollno.data, std_class=std_class)  

        db.session.add(std_to_create)
        db.session.commit()
        return redirect(url_for('info_page', classid=std_class))

    if form.errors !={} :
        for err_msg in form.errors.values():
            flash(f'There was an error with creating new student:{err_msg}', category='danger')
    return render_template('/addentity/addstudent.html', form=form,std_class = std_class )



#camera capture
@app.route('/<classid>/classattendance')
def class_info(classid):
    class_id=classid
    classinfo = Allclasses.query.filter_by(id=class_id).first()
    return render_template('/capture/camcaptureclass.html', class_id=class_id, classinfo = classinfo)

@app.route('/<classid>/takeattendance')
def video_feed(classid):
    classid=classid
    known_face_encodings = get_face_encodings(classid)
    known_face_names = get_face_names(classid)
    return Response(gen_frames(known_face_encodings, known_face_names, classid), mimetype='multipart/x-mixed-replace; boundary=frame')



#screen capture
@app.route('/<classid>/screen_attendance')
def class_screen(classid):
    class_id=classid
    classinfo = Allclasses.query.filter_by(id=class_id).first()
    return render_template('/capture/screencaptureclass.html', class_id=class_id, classinfo = classinfo)

@app.route('/<classid>/takeattendance_usingscreen')
def screen_feed(classid):
    classid=classid
    known_face_encodings = get_face_encodings(classid)
    known_face_names = get_face_names(classid)
    return Response(gen_shots(known_face_encodings, known_face_names, classid), mimetype='multipart/x-mixed-replace; boundary=frame')



#donload csv file for attendance
@app.route('/downloadreport')
def download_csv():   

    csv_list = Student.query.with_entities(Student.std_id, Student.std_name, Student.std_attendance).filter_by(std_class=1)
   
    output = io.StringIO()
    writer = csv.writer(output)

    line = ['Id, Name, Attendance']
    writer.writerow(line)

    for row in csv_list:
        line = [str(row.std_id) + ',' + row.std_name + ',' + str(row.std_attendance) ]
        writer.writerow(line)

    output.seek(0)   
    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=Attendance_report.csv"})



#delete a student
@app.route('/<stdid>/deletestd')
def delete_std(stdid):
    stdid=stdid
    Student.query.filter_by(std_id=stdid).delete()
    db.session.commit()
