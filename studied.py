import models, vul, os
from flask import request, send_file
from PIL import Image


def create_student():
    form = request.form
    files = request.files
    lastname = form['surname']
    firstname = form['firstname']
    sex = form['sex']
    dob_str = form['dob']
    ssn = form['ssn']
    passportn = form['passport_number']
    addresss = form['address']
    phonen = form['phonen']
    email = form['email']
    bn = form['bn']
    acc = form['acc']
    region = form['region']
    branch = form['branch']
    rol = mycity = form['mycity']
    nationality = form['nationality']
    employer = form['employer']
    role = form['role']
    course = form['course']
    university = form['university']
    gradyear = form['grad_year']
    myclass = form['myclass']
    fromcountry = form['fromcountry']
    destination = form['destination']
    tostudy = course

    passport = files.get('passport')
    cv = files.get('cv')
    degree = files.get('degree')
    transcript = files.get('transcript')
    wassce = files.get('wassce')

    # Save student to the database
    # Save student to the database
    student = models.Student(
        firstname=firstname,
        lastname=lastname,
        sex=sex,
        dob=dob_str,  # Assuming dob is already parsed into a date object
        ssn=ssn,
        passportn=passportn,
        address=addresss,  # Assuming you meant addresss instead of address typo
        phonen=phonen,
        email=email,
        bn=bn,
        acc=acc,
        region=region,
        branch=branch,
        mycity=mycity,
        rol=rol,
        nationality=nationality,
        employer=employer,
        role=role,
        course=course,
        university=university,
        gradyear=gradyear,
        myclass=myclass,
        fromcountry=fromcountry,
        destination=destination,
        tostudy=tostudy,
        student_status='new',
        cv=cv.filename
    )

    models.db.session.add(student)
    models.db.session.commit()

    folder_name = str(student.id) + '_' + firstname + '_' + lastname
    student_folder = os.path.join('students', folder_name)
    os.makedirs(student_folder, exist_ok=True)

    if passport.filename != '':
        pdf_path = os.path.join(student_folder, "passport.pdf")
        file_extension = passport.filename.split('.')[-1].lower()
        if file_extension in ['jpg', 'jpeg', 'png']:
            image = Image.open(passport)
            image.convert('RGB').save(pdf_path)
        else:
            passport.save(pdf_path)

    if cv.filename != '':
        pdf_path = os.path.join(student_folder, "cv.pdf")
        cv.save(pdf_path)

    if degree.filename != '':
        pdf_path = os.path.join(student_folder, "degree.pdf")
        degree.save(pdf_path)

    if transcript.filename != '':
        pdf_path = os.path.join(student_folder, "transcript.pdf")
        transcript.save(pdf_path)

    if wassce.filename != '':
        pdf_path = os.path.join(student_folder, "wassce.pdf")
        wassce.save(pdf_path)


    return "good"
