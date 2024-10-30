from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify, send_from_directory, abort
from ext import db, bcrypt
from forms import RegistrationForm, LoginForm
from models import User, Visitor
from flask_login import login_user, current_user, logout_user, login_required
import models, os, visited, things, studied, studieded, get_emails

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ATTACHMENTS_FOLDER = os.path.join(os.getcwd(), 'attachments')
os.makedirs(ATTACHMENTS_FOLDER, exist_ok=True)

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
@main_blueprint.route('/home')
@login_required
def home():
    return render_template('home.html')

@main_blueprint.route('/download/<filename>')
def download_file(filename):
    """Serve the attachment file for download."""
    try:
        return send_from_directory(
            ATTACHMENTS_FOLDER, filename, as_attachment=True
        )
    except FileNotFoundError:
        abort(404)

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.new_student'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in',
              'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.inbox'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(
                url_for('main.inbox'))
        else:
            flash('Login Unsuccessful. Please check email and password',
                  'danger')
    return render_template('login.html', title='Login', form=form)


@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main_blueprint.route('/new_visitor', methods=['GET', 'POST'])
@login_required
def new_visitor():
    return things.upload_v_file('uploads/', 'new_visitor')


@main_blueprint.route('/create_visitor', methods=['POST'])
@login_required
def create_visitor():
    visited.create_visitor()
    return redirect(url_for('main.visitors'))


@main_blueprint.route('/visitors')
@login_required
def visitors():
    visitors = models.Visitor.query.order_by(models.Visitor.id.desc()).all()
    return render_template('visitors.html', visitors=visitors)


@main_blueprint.route('/visitors/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_visitor(id):
    visitor = models.Visitor.query.get_or_404(id)
    if request.method == 'POST':
        visitor.firstname = request.form['firstname']
        visitor.lastname = request.form['lastname']
        # Update other fields as necessary
        db.session.commit()
        return redirect(url_for('main.visitors'))
    return render_template('edit_visitor.html', visitor=visitor)


@main_blueprint.route('/visitors/delete/<int:id>', methods=['POST'])
@login_required
def delete_visitor(id):
    visitor = models.Visitor.query.get_or_404(id)
    db.session.delete(visitor)
    db.session.commit()
    return redirect(url_for('main.visitors'))


@main_blueprint.route('/new_student', methods=['GET', 'POST'])
@login_required
def new_student():
    return things.upload_file('uploads/', 'new_student')


@main_blueprint.route('/create_student', methods=['POST'])
@login_required
def create_student():
    studied.create_student()
    return redirect(url_for('main.new_student'))

@main_blueprint.route('/gen_student', methods=['GET'])
@login_required
def gen_student():
    studieded.gen_student()
    return redirect(url_for('main.inbox'))


@main_blueprint.route('/students')
@login_required
def students():
    students = models.Student.query.order_by(models.Student.id.desc()).all()
    return render_template('students.html', students=students)


@main_blueprint.route('/inbox')
@login_required
def inbox():
    emails = get_emails.get_mails()
    return render_template('inbox.html', emails=emails)


@main_blueprint.route('/studentsapi/<int:id>', methods=['GET'])
def studentapi(id):
    student = models.Student.query.get_or_404(id)

    # Convert the student object to a dictionary
    student_dict = student.to_dict()

    # Return the student details as JSON
    return jsonify(student_dict)


@main_blueprint.route('/studentsapi')
def studentsapi():
    students = models.Student.query.order_by(models.Student.id.desc()).all()
    students_list = [student.to_dict() for student in students]
    return jsonify(students_list)


# Update a specific student's details by ID
@main_blueprint.route('/studentsapi/update/<int:id>', methods=['PATCH', 'PUT'])
def update_studentapi(id):
    student = models.Student.query.get_or_404(id)

    # Get the JSON data from the request
    data = request.get_json()

    # Update fields that are provided in the request
    if 'firstname' in data:
        student.firstname = data['firstname']
    if 'lastname' in data:
        student.lastname = data['lastname']
    if 'student_status' in data:
        student.student_status = data['student_status']
    if 'sex' in data:
        student.sex = data['sex']
    if 'dob' in data:
        student.dob = data['dob']
    if 'ssn' in data:
        student.ssn = data['ssn']
    if 'passportn' in data:
        student.passportn = data['passportn']
    if 'address' in data:
        student.address = data['address']
    if 'phonen' in data:
        student.phonen = data['phonen']
    if 'email' in data:
        student.email = data['email']
    if 'bn' in data:
        student.bn = data['bn']
    if 'acc' in data:
        student.acc = data['acc']
    if 'region' in data:
        student.region = data['region']
    if 'branch' in data:
        student.branch = data['branch']
    if 'mycity' in data:
        student.mycity = data['mycity']
    if 'rol' in data:
        student.rol = data['rol']
    if 'nationality' in data:
        student.nationality = data['nationality']
    if 'employer' in data:
        student.employer = data['employer']
    if 'course' in data:
        student.course = data['course']
    if 'university' in data:
        student.university = data['university']
    if 'gradyear' in data:
        student.gradyear = data['gradyear']
    if 'myclass' in data:
        student.myclass = data['myclass']
    if 'fromcountry' in data:
        student.fromcountry = data['fromcountry']
    if 'destination' in data:
        student.destination = data['destination']
    if 'tostudy' in data:
        student.tostudy = data['tostudy']

    # Commit the changes to the database
    models.db.session.commit()

    # Return a success response
    return jsonify({"message": "Student updated successfully!"}), 200


# Get visitor details by ID
@main_blueprint.route('/visitorsapi/<int:id>', methods=['GET'])
def visitorapi(id):
    visitor = Visitor.query.get_or_404(id)

    # Convert the visitor object to a dictionary
    visitor_dict = visitor.to_dict()

    # Return the visitor details as JSON
    return jsonify(visitor_dict)


# Get all visitors, ordered by ID in descending order
@main_blueprint.route('/visitorsapi', methods=['GET'])
def visitorsapi():
    visitors = Visitor.query.order_by(Visitor.id.desc()).all()
    visitors_list = [visitor.to_dict() for visitor in visitors]
    return jsonify(visitors_list)


# Update a specific visitor's details by ID
@main_blueprint.route('/visitorsapi/update/<int:id>', methods=['PATCH', 'PUT'])
def update_visitorapi(id):
    visitor = Visitor.query.get_or_404(id)

    # Get the JSON data from the request
    data = request.get_json()

    # Update fields that are provided in the request
    if 'firstname' in data:
        visitor.firstname = data['firstname']
    if 'lastname' in data:
        visitor.lastname = data['lastname']
    if 'sex' in data:
        visitor.sex = data['sex']
    if 'dob' in data:
        visitor.dob = data['dob']
    if 'ssn' in data:
        visitor.ssn = data['ssn']
    if 'passportn' in data:
        visitor.passportn = data['passportn']
    if 'addresss' in data:
        visitor.addresss = data['addresss']
    if 'phonen' in data:
        visitor.phonen = data['phonen']
    if 'bn' in data:
        visitor.bn = data['bn']
    if 'acc' in data:
        visitor.acc = data['acc']
    if 'region' in data:
        visitor.region = data['region']
    if 'branch' in data:
        visitor.branch = data['branch']
    if 'rol' in data:
        visitor.rol = data['rol']
    if 'nationality' in data:
        visitor.nationality = data['nationality']
    if 'spouse_name' in data:
        visitor.spouse_name = data['spouse_name']
    if 'spouse_last' in data:
        visitor.spouse_last = data['spouse_last']
    if 'child1name' in data:
        visitor.child1name = data['child1name']
    if 'child2name' in data:
        visitor.child2name = data['child2name']
    if 'fathername' in data:
        visitor.fathername = data['fathername']
    if 'fatherlast' in data:
        visitor.fatherlast = data['fatherlast']
    if 'fatherwork' in data:
        visitor.fatherwork = data['fatherwork']
    if 'mothername' in data:
        visitor.mothername = data['mothername']
    if 'motherwork' in data:
        visitor.motherwork = data['motherwork']
    if 'visited' in data:
        visitor.visited = data['visited']
    if 'conference' in data:
        visitor.conference = data['conference']
    if 'destination' in data:
        visitor.destination = data['destination']
    if 'visitor_status' in data:
        visitor.destination = data['visitor_status']

    # Commit the changes to the database
    db.session.commit()

    # Return a success response
    return jsonify({"message": "Visitor updated successfully!"}), 200
