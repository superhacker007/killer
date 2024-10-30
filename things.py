import io, os, vul
from flask import request, render_template, redirect
from google.cloud import vision
import fitz, time
from num2words import num2words


def extract_image_from_pdf(pdf_path):
    """Extract the first image from the first page of a PDF file."""
    document = fitz.open(pdf_path)
    page = document.load_page(0)  # Get the first page
    images = page.get_images(full=True)
    if not images:
        raise ValueError("No images found in the PDF")
    
    # Extract the first image
    image_index = images[0][0]
    base_image = document.extract_image(image_index)
    image_bytes = base_image["image"]
    return io.BytesIO(image_bytes)

def extract_text_from_image(image_content):
    """Extract text from an image using Google Cloud Vision API."""
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=image_content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f'{response.error.message}')

    full_text = texts[0].description if texts else ''
    return full_text

def extract_passport_details(image_content):
    """Extract details from passport image using Google Cloud Vision API."""
    full_text = extract_text_from_image(image_content)
    details = parse_passport_details(full_text)
    return details

def parse_passport_details(text):
    """Parse passport details from the detected text."""
    lines = text.split('\n')
    passport_details = {}
    label_to_key = {
        'Passport No': 'passport_number',
        'No de passeport': 'passport_number',
        'Surname': 'surname',
        'Nom': 'surname',
        'Given Name': 'firstname',
        'Prenoms': 'firstname',
        'Nationality': 'nationality',
        'Nationality': 'nationality',
        'Date of birth': 'dob',
        'Date de naissance': 'dob',
        'Sex': 'sex',
        'Sexe': 'sex',
        'Place of Birth': 'place_of_birth',
        'Lieu de naissance': 'place_of_birth',
        'Date of expiry': 'expiry_date',
        'Date d’expiration': 'expiry_date',
    }

    last_label = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if last_label:
            passport_details[last_label] = line
            last_label = None
            continue

        for label, key in label_to_key.items():
            if label in line:
                last_label = key
                break

    return passport_details

def extract_certificate_details(image_content):
    """Extract details from a university certificate using Google Cloud Vision API."""
    full_text = extract_text_from_image(image_content)
    details = parse_certificate_details(full_text)
    return details

def parse_certificate_details(text):
    """Parse certificate details from the detected text."""
    lines = text.split('\n')
    certificate_details = {
        'school_name': '',
        'course_name': '',
        'graduation_date': ''
    }

    if lines:
        certificate_details['school_name'] = lines[0]  # Assuming the school name is at the top
        certificate_details['course_name'] = lines[-2]  # Assuming the course name is second from the bottom
        certificate_details['graduation_date'] = lines[-1]  # Assuming the graduation date is at the bottom

    return certificate_details

def upload_v_file(upload_folder, go_to):
    if request.method == 'POST':
        passport_file = request.files.get('passport')

        if not passport_file:
            return "Passport file is required", 400

        # Save and process passport file
        passport_file_path = os.path.join(upload_folder, passport_file.filename)
        passport_file.save(passport_file_path)

        if passport_file.filename.lower().endswith('.pdf'):
            passport_image_content = extract_image_from_pdf(passport_file_path).read()
        else:
            with open(passport_file_path, 'rb') as image_file:
                passport_image_content = image_file.read()

        personal_info = extract_passport_details(passport_image_content)

        
        details = {
            **personal_info
        }

        return render_template(f'{go_to}.html', details=details)

    return render_template(f'{go_to}.html')

def upload_file(upload_folder, go_to):
    if request.method == 'POST':
        passport_file = request.files.get('passport')
        degree_file = request.files.get('degree')
        high_school_file = request.files.get('high_school')

        if not passport_file:
            return "Passport file is required", 400

        # Save and process passport file
        passport_file_path = os.path.join(upload_folder, passport_file.filename)
        passport_file.save(passport_file_path)

        if passport_file.filename.lower().endswith('.pdf'):
            passport_image_content = extract_image_from_pdf(passport_file_path).read()
        else:
            with open(passport_file_path, 'rb') as image_file:
                passport_image_content = image_file.read()

        personal_info = extract_passport_details(passport_image_content)

        degree_info = {}
        if degree_file:
            # Save and process degree file
            degree_file_path = os.path.join(upload_folder, degree_file.filename)
            degree_file.save(degree_file_path)

            if degree_file.filename.lower().endswith('.pdf'):
                degree_image_content = extract_image_from_pdf(degree_file_path).read()
            else:
                with open(degree_file_path, 'rb') as image_file:
                    degree_image_content = image_file.read()

            degree_info = extract_certificate_details(degree_image_content)

        high_school_info = {}
        if high_school_file:
            # Save and process high school file
            high_school_file_path = os.path.join(upload_folder, high_school_file.filename)
            high_school_file.save(high_school_file_path)

            if high_school_file.filename.lower().endswith('.pdf'):
                high_school_image_content = extract_image_from_pdf(high_school_file_path).read()
            else:
                with open(high_school_file_path, 'rb') as image_file:
                    high_school_image_content = image_file.read()

            high_school_info = extract_certificate_details(high_school_image_content)
        ssn_number = vul.random.randint(100000000, 999999999)
        dash = vul.random.randint(0,9)
        acc = vul.random.randint(200000000000, 209999999999)
        details = {
            **personal_info,
            'degree': degree_info,
            'high_school': high_school_info,
            'ssn': "GHA-" + str(ssn_number) + "-" + str(dash),
            'acc': acc,
        }

        return render_template(f'{go_to}.html', details=details)

    return render_template(f'{go_to}.html')

def get_network(phonen):
    
    if phonen[:3] == "024" or phonen[:3] == "054" or phonen[:3] == "059" or phonen[:3] == "055" or phonen[:3] == "053":
        network = "MTN"
    elif phonen[:3] == "020" or phonen[:3] == "050":
        network = "TELECEL"
    else:
        network = "AT"
    
    return network

def convert_amount_to_words(amount):
    # Separate the Cedis and Pesewas
    cedis, pesewas = divmod(amount, 1)
    cedis = int(cedis)
    pesewas = round(pesewas * 100)

    # Convert Cedis and Pesewas to words
    cedi_words = num2words(cedis, lang='en')
    pesewa_words = num2words(pesewas, lang='en')

    # Combine the Cedi and Pesewa words
    if pesewas > 0:
        result = f"{cedi_words} cedis, {pesewa_words} pesewas"
    else:
        result = f"{cedi_words} cedis"

    return result.capitalize()


def get_first_name(full_name):
    # Split the full name by spaces
    name_parts = full_name.split()
    
    # Return the first part as the first name
    # If the name_parts list is empty, return an empty string
    return name_parts[0] if name_parts else ''