from ext import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    dob = db.Column(db.String(40))
    ssn = db.Column(db.String(100))
    passportn = db.Column(db.String(100))
    address = db.Column(db.String(500))
    phonen = db.Column(db.String(100))
    email = db.Column(db.String(100))
    bn = db.Column(db.String(100))
    acc = db.Column(db.String(100))
    region = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    mycity = db.Column(db.String(100))
    rol = db.Column(db.String(100))
    nationality = db.Column(db.String(100))
    employer = db.Column(db.String(100))
    role = db.Column(db.String(100))
    university = db.Column(db.String(500))
    gradyear = db.Column(db.String(100))
    myclass = db.Column(db.String(100))
    fromcountry = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    tostudy = db.Column(db.String(100))
    cv = db.Column(db.String(100))

    # Existing columns
    school = db.Column(db.String(500))
    # college = db.Column(db.String(500))
    # department1 = db.Column(db.String(500))
    # department2 = db.Column(db.String(500))
    course = db.Column(db.String(500))
    # startyear = db.Column(db.String(100))
    # endyear = db.Column(db.String(100))
    # classe = db.Column(db.String(500))
    # division = db.Column(db.String(100))
    student_status = db.Column(db.String(10))

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "sex": self.sex,
            "dob": self.dob,
            "ssn": self.ssn,
            "passportn": self.passportn,
            "address": self.address,
            "phonen": self.phonen,
            "email": self.email,
            "bn": self.bn,
            "acc": self.acc,
            "region": self.region,
            "branch": self.branch,
            "mycity": self.mycity,
            "rol": self.rol,
            "nationality": self.nationality,
            "employer": self.employer,
            "role": self.employer,
            "university": self.university,
            "gradyear": self.gradyear,
            "myclass": self.myclass,
            "fromcountry": self.fromcountry,
            "destination": self.destination,
            "tostudy": self.tostudy,
            # Existing fields
            "school": self.school,
            # "college": self.college,
            # "department1": self.department1,
            # "department2": self.department2,
            "course": self.course,
            # "startyear": self.startyear,
            # "endyear": self.endyear,
            # "classe": self.classe,
            # "division": self.division,
            "student_status": self.student_status,
            "cv":self.cv
        }


class Visitor(db.Model):
    __tablename__ = 'visitors'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    city = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    dob = db.Column(db.String(40))
    ssn = db.Column(db.String(100))
    passportn = db.Column(db.String(100))
    addresss = db.Column(db.String(100))
    phonen = db.Column(db.String(100))
    bn = db.Column(db.String(100))
    acc = db.Column(db.String(100))
    region = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    rol = db.Column(db.String(100))
    start_date = db.Column(db.String(100))
    enddate = db.Column(db.String(100))
    hassal = db.Column(db.String(100))
    nationality = db.Column(db.String(100))
    spouse_name = db.Column(db.String(100))
    spouse_last = db.Column(db.String(100))
    child1name = db.Column(db.String(100))
    child2name = db.Column(db.String(100))
    fathername = db.Column(db.String(100))
    fatherlast = db.Column(db.String(100))
    fatherwork = db.Column(db.String(100))
    mothername = db.Column(db.String(100))
    motherwork = db.Column(db.String(100))
    visited = db.Column(db.String(100))
    conference = db.Column(db.String(100))
    visitor_status = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'destination': self.destination,
            'city': self.city,
            'sex': self.sex,
            'dob': self.dob,
            'ssn': self.ssn,
            'passportn': self.passportn,
            'addresss': self.addresss,
            'phonen': self.phonen,
            'bn': self.bn,
            'acc': self.acc,
            'region': self.region,
            'branch': self.branch,
            'rol': self.rol,
            'start_date': self.start_date,
            'enddate': self.enddate,
            'hassal': self.hassal,
            'nationality': self.nationality,
            'spouse_name': self.spouse_name,
            'spouse_last': self.spouse_last,
            'child1name': self.child1name,
            'child2name': self.child2name,
            'fathername': self.fathername,
            'fatherlast': self.fatherlast,
            'fatherwork': self.fatherwork,
            'mothername': self.mothername,
            'motherwork': self.motherwork,
            'visited': self.visited,
            'conference': self.conference,
            'visitor_status': self.visitor_status
        }
