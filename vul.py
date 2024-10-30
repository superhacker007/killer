from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import random, smtplib, pdfkit, os, inflect, string, datas, dateutil.parser
from flask import render_template
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError
import PyPDF2
import pikepdf
from openai import OpenAI
import numpy as np

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

path_to_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'  # Use the correct path from 'which wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)


places = ''
# Helper function to get day suffix
def get_day_suffix(day):
    return "th" if 4 <= day <= 20 or 24 <= day <= 30 else ["st", "nd", "rd"][day % 10 - 1]

# Format date with suffix
def day_with_suffix(date_object):
    day = date_object.day
    return f"{day}{get_day_suffix(day)} {date_object.strftime('%B, %Y')}"

# Ensure the date is a weekday
def make_monday_if_weekend(date_obj):
    return date_obj + timedelta(days=(7 - date_obj.weekday()) % 7) if date_obj.weekday() > 4 else date_obj

# Format date with suffix
def format_date_with_suffix(date):
    suffix = 'th' if 10 < date.day < 14 else {1: 'st', 2: 'nd', 3: 'rd'}.get(date.day % 10, 'th')
    return date.strftime(f'%d{suffix} %B %Y').lstrip('0')


# Extract last two digits of the year
def get_last_two_digits_of_year(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').year % 100

# Extract month from date string
def get_month_from_date_str(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%m')

# Subtract days ensuring a business day
def subtract_days(days):
    return make_monday_if_weekend(date.today() - timedelta(days=days))

# Generate random name
def generate_random_name():
    return f"{random.choice(datas.first_male_names)} {random.choice(datas.last_names)}"

# Generate random transaction ID
def generate_random_trans_id(length):
    return ''.join(random.choices(string.digits, k=length))

# Generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Format date
def formatmydate(today=datetime.now(), formatas="dd/mm/yyyy"):
    return today.strftime(formatas)

# Convert date string to datetime object
def objme(date_str):
    try:
        # Use dateutil.parser to parse the date string automatically
        parsed_date = dateutil.parser.parse(date_str)
        return parsed_date
    except ValueError:
        raise ValueError(f"Unable to parse the date: {date_str}")


# Convert number to words
def number_to_words(num):
    p = inflect.engine()
    return p.number_to_words(num).replace(',', '')

def syear(start_date):
    # Returns the difference in years between the current date and the start date
    return datetime.now().year - start_date.year

def format_date_with_suffix_split(date):
    # Determine the correct suffix for the day
    suffix = 'th' if 10 < date.day < 14 else {1: 'st', 2: 'nd', 3: 'rd'}.get(date.day % 10, 'th')
    
    # Format the day without leading zeros and append the suffix
    day_format = date.strftime('%d').lstrip('0') + suffix
    
    # Return day with suffix, month, and year
    return day_format, date.strftime('%B'), date.strftime('%Y')

def subtract_years_months(years=0, months=0):
    # Subtract specified years and months from the current date
    return datetime.now() - relativedelta(years=years, months=months)

# Get places
def getplaces(num, destinations):
    if destinations.lower() == "sydney":
        places = datas.available_places_sydney
    elif destinations.lower() == "lisbon":
        places = datas.available_places_lisbon
    elif destinations.lower() == "toronto":
        places = datas.available_places_toronto
    elif destinations.lower() == "quebec":
        places = datas.available_places_quebec
    elif destinations.lower() == "vancouver":
        places = datas.available_places_vancouver
    elif destinations.lower() == "tirana":
        places = datas.available_places_albania
    return random.sample(places[1:], num) if len(places) > num else places[1:]

# Get hotel
def gethotel(destinations):
    if destinations.lower() == "sydney":
        hotels = datas.hotels_sydney
    elif destinations.lower() == "quebec":
        hotels = datas.hotels_quebec
    elif destinations.lower() == "lisbon":
        hotels = datas.hotels_lisbon
    elif destinations.lower() == "vancouver":
        hotels = datas.hotels_vancouver
    elif destinations.lower() == "toronto":
        hotels = datas.hotels_toronto
    elif destinations.lower() == "tirana":
        hotels = datas.hotels_albania
    return [hotels[0]] + random.sample(hotels[1:], 1)

# Get conference
def getconference(id):
    return datas.conferences[id]

# Random generator class
class RandomGenerator:
    def generate_random_numbers(self, start, end, count):
        return np.random.randint(start, end + 1, size=count).tolist()

    def generate_deep_colors(self, count):
        return [f"#{random.randint(128, 255):02x}{random.randint(0, 127):02x}{random.randint(0, 127):02x}" for _ in range(count)]

# Social Security Number
ssn = f'C00{random.randint(1, 10)}X'

# Send email
def send_email(recipient_email, subject, body, attachment_paths=None):
    try:
        recipient_email = validate_email(recipient_email)["email"]
    except EmailNotValidError as e:
        print(f"Invalid email address: {str(e)}")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = "tickets@waaptravels.com"
    msg['To'] = recipient_email
    msg.set_content(body)
    msg.add_alternative(body, subtype='html')

    if attachment_paths:
        for attachment_path in attachment_paths:
            try:
                with open(attachment_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=os.path.basename(attachment_path))
            except Exception as e:
                print(f"Failed to attach file {attachment_path}: {e}")
                return

    try:
        with smtplib.SMTP_SSL('smtp.titan.email', 465) as server:
            server.login("tickets@waaptravels.com", "GreatNews@2024")
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Render HTML to PDF
def render_html_to_pdf(template_name, output_html_path, output_pdf_path, template_vars, options):
    html_content = render_template(template_name, **template_vars)
    with open(output_html_path, 'w') as file:
        file.write(html_content)
    pdfkit.from_file(output_html_path, output_pdf_path, options=options)
    os.remove(output_html_path)

# Render HTML to file
def render_html_to_file(template_name, output_html_path, template_vars, options):
    html_content = render_template(template_name, **template_vars)
    with open(output_html_path, 'w') as file:
        file.write(html_content)

# Get document paths
def get_document_paths(visitor_folder, base_filename):
    base_path = os.path.join(visitor_folder, base_filename)
    return f"{base_path}.html", f"{base_path}.pdf"

# Process date
def process_date(date_obj):
    formatted_date = format_date_with_suffix(date_obj)
    year_last_two = get_last_two_digits_of_year(date_obj.strftime('%Y-%m-%d'))
    month_str = get_month_from_date_str(date_obj.strftime('%Y-%m-%d'))
    return formatted_date, year_last_two, month_str

# Get ordinal representation of a number
def get_ordinal(n):
    suffix = 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

# Extract date parts
def extract_date_parts(years, weeks):
    date_obj = (date.today() - relativedelta(years=years) - timedelta(weeks=weeks))
    day = get_ordinal(date_obj.day)
    month_name = date_obj.strftime("%B")
    year_last_two = date_obj.strftime("%y")
    p = inflect.engine()
    year_last_two_word = p.number_to_words(year_last_two).capitalize()
    return (day, month_name, year_last_two, year_last_two_word)

# Get formatted date
def get_formatted_date(dated=None):
    return (dated or date.today()).strftime("%d/%m/%Y")

# Subtract month and format date
def subtract_month_and_format(date_obj):
    return (date_obj - relativedelta(months=1)).strftime('%Y-%m-%d')

# Add days and format date
def add_day_and_format(date_obj, days):
    return format_date_with_suffix(date_obj + timedelta(days=days))

# Get day and month
def get_day_and_month(date_obj, days):
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime('%d'), new_date.strftime('%B')

# Get formatted date with time
def get_formatted_dated():
    return datetime.now().strftime("%d %B %Y")

# Generate random characters
def generate_random_chars():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

# Format date to month and day
def format_date_to_month_day():
    return datetime.now().strftime('%B %d')

# Format day
def format_my_day(date_obj):
    return date_obj.strftime('%B %d, %Y')

# Parse date
def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

# Plan trip activities with places
def plan_trip_activities_with_places(conferenced):
    conference_start = parse_date(conferenced[1])
    total_days = random.randint(13, 17)
    conference_end = conference_start + timedelta(days=1)
    departure_day = conference_end + timedelta(days=1)
    trip_start_date = conference_start - timedelta(days=total_days - 3)
    itinerary = []
    current_day_index = 1
    random.shuffle(datas.available_places)
    while current_day_index < total_days - 3:
        if not datas.available_places:
            break
        selected_place = datas.available_places.pop()
        if current_day_index + 1 < total_days - 3:
            itinerary.append([f"Day {current_day_index} to Day {current_day_index + 1}", selected_place[0], selected_place[1], selected_place[2], selected_place[3]])
            current_day_index += 2
        else:
            itinerary.append([f"Day {current_day_index}", selected_place[0], selected_place[1], selected_place[2], selected_place[3]])
            current_day_index += 1
    itinerary.append([f"Day {total_days - 2} to Day {total_days - 1}", conferenced[0], conferenced[2], conferenced[9], "../gca"])
    itinerary.append([f"Day {total_days}", "Departure", "Day of departure", conferenced[9], "../dep"])
    return itinerary, total_days, trip_start_date.strftime('%Y-%m-%d'), departure_day.strftime('%Y-%m-%d'), conferenced[9]

from datetime import datetime, timedelta
import random

def calculate_employment_start_date(dob):
    dob_year = dob.year
    current_year = 2024
    if dob_year > 2000:
        years_ago = random.randint(1, 3)
    elif 1990 < dob_year <= 2000:
        years_ago = random.randint(4, 8)
    elif 1980 < dob_year <= 1990:
        years_ago = random.randint(8, 20)
    else:
        years_ago = random.randint(20, 30)
    
    start_year = current_year - years_ago
    start_month = random.randint(1, 12)
    
    # Determine the last day of the month
    if start_month in [1, 3, 5, 7, 8, 10, 12]:
        last_day = 31
    elif start_month in [4, 6, 9, 11]:
        last_day = 30
    else:
        # February: check for leap year
        if (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0):
            last_day = 29
        else:
            last_day = 28
    
    start_day = random.randint(1, last_day)
    
    return datetime(start_year, start_month, start_day).strftime('%Y-%m-%d')

def calculate_employment_start_date_for_daddy(dob):
    dob_year = dob.year
    current_year = 2024
    if dob_year > 2000:
        years_ago = random.randint(15, 25)
    elif 1990 < dob_year <= 2000:
        years_ago = random.randint(25, 30)
    else:
        years_ago = random.randint(30, 40)
    
    start_year = current_year - years_ago
    start_month = random.randint(1, 12)
    
    # Determine the last day of the month
    if start_month in [1, 3, 5, 7, 8, 10, 12]:
        last_day = 31
    elif start_month in [4, 6, 9, 11]:
        last_day = 30
    else:
        # February: check for leap year
        if (start_year % 4 == 0 and start_year % 100 != 0) or (start_year % 400 == 0):
            last_day = 29
        else:
            last_day = 28
    
    start_day = random.randint(1, last_day)
    
    return datetime(start_year, start_month, start_day).strftime('%Y-%m-%d')

# Merge PDFs
def merge_pdfs(directory, pdf_list, output):
    pdf_merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        pdf_merger.append(os.path.join(directory, pdf))
    output_path = os.path.join(directory, output)
    with open(output_path, 'wb') as out:
        pdf_merger.write(out)
    return output_path

# Merge different PDFs
def merge_diff_pdfs(pdf_paths, output_directory, output_filename):
    pdf_merger = PyPDF2.PdfMerger()
    for pdf_path in pdf_paths:
        pdf_merger.append(pdf_path)
    output_path = os.path.join(output_directory, output_filename)
    with open(output_path, 'wb') as out:
        pdf_merger.write(out)
    return output_path

# Compress PDF
def compress_pdf(input_path, output_path):
    try:
        with pikepdf.open(input_path) as pdf:
            pdf.save(output_path, linearize=True)
        print(f"Compressed {input_path} to {output_path}")
    except Exception as e:
        print(f"Failed to compress file {input_path}: {e}")

# Compress PDF to target size
def compress_pdf_last(input_path, output_path, target_size_mb=2, initial_quality=95):
    try:
        quality = initial_quality
        while True:
            with pikepdf.open(input_path) as pdf:
                pdf.save(output_path, linearize=True)
            file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"Compressed to {file_size_mb:.2f} MB")
            if file_size_mb < target_size_mb or quality < 1:
                break
            quality -= 10
            print(f"Reducing quality to {quality}")
        print(f"Final compressed size: {file_size_mb:.2f} MB")
    except Exception as e:
        print(f"Failed to compress file {input_path}: {e}")

# List of male first names
first_male_names = ['Kwame', 'Kojo', 'Kofi', 'Yaw', 'Kwesi', 'Kwabena', 'Kwaku', 'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Charles', 'Thomas', 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Mark', 'Paul', 'Steven', 'Andrew', 'Kenneth', 'Joshua', 'George', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan', 'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon', 'Frank', 'Benjamin', 'Gregory', 'Samuel', 'Raymond', 'Patrick', 'Alexander', 'Jack', 'Dennis', 'Jerry', 'Tyler', 'Aaron', 'Jose', 'Henry', 'Douglas', 'Adam', 'Peter', 'Nathan', 'Zachary', 'Walter', 'Kyle', 'Harold', 'Carl', 'Jeremy', 'Keith', 'Roger', 'Gerald', 'Ethan', 'Arthur', 'Terry', 'Christian', 'Sean', 'Lawrence', 'Austin', 'Joe', 'Noah', 'Jesse', 'Albert', 'Bryan', 'Billy', 'Bruce', 'Willie', 'Jordan', 'Dylan', 'Alan', 'Ralph', 'Gabriel', 'Roy', 'Juan', 'Wayne', 'Eugene', 'Logan', 'Randy', 'Louis', 'Russell', 'Vincent', 'Philip', 'Bobby', 'Johnny', 'Bradley']

# Get random farm
def get_my_farm():
    return random.choice(datas.land_at)

# List of female first names
first_female_names = ['Abena', 'Akua', 'Esi', 'Efua', 'Adjoa', 'Akosua', 'Yaa', 'Ama', 'Afia', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen', 'Nancy', 'Lisa', 'Margaret', 'Betty', 'Sandra', 'Ashley', 'Dorothy', 'Kimberly', 'Emily', 'Donna', 'Michelle', 'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Sharon', 'Laura', 'Cynthia', 'Kathleen', 'Amy', 'Shirley', 'Angela', 'Helen', 'Anna', 'Brenda', 'Pamela', 'Nicole', 'Samantha', 'Katherine', 'Christine', 'Debra', 'Rachel', 'Carolyn', 'Janet', 'Catherine', 'Maria', 'Heather', 'Diane', 'Ruth', 'Julie', 'Olivia', 'Joyce', 'Virginia', 'Victoria', 'Kelly', 'Lauren', 'Christina', 'Joan', 'Evelyn', 'Judith', 'Megan', 'Cheryl', 'Andrea', 'Hannah', 'Martha', 'Jacqueline', 'Frances', 'Gloria', 'Ann', 'Teresa', 'Kathryn', 'Sara', 'Janice', 'Jean', 'Alice', 'Madison', 'Doris', 'Abigail', 'Julia', 'Judy', 'Grace', 'Denise', 'Amber', 'Marilyn', 'Beverly', 'Danielle', 'Theresa', 'Sophia', 'Marie', 'Diana', 'Brittany', 'Natalie', 'Isabella', 'Charlotte', 'Rose', 'Alexis', 'Kayla', 'Ella']

# Generate random first names for male and female friends
def random_male_friend_firstname():
    return random.choice(first_male_names)

def random_female_friend_firstname():
    return random.choice(first_female_names)

# Get random friend
def get_random_friend():
    return random.choice(datas.friends_list)

# Get previous travel
def previous_travel():
    
    return random.choice(datas.travels)

# Get nice date
def nice_date(date_obj):
    return datetime(date_obj).strftime("%B %d, %Y")

# Move date ensuring working day
def move_date(original_date, weeks_to_add):
    new_date = original_date + relativedelta(weeks=weeks_to_add)
    while new_date.weekday() > 4:
        new_date += timedelta(days=1)
    return new_date

# Generate transactions
def generate_transactions(closing_balance, num_transactions):
    transactions = []
    current_balance = closing_balance
    date = datetime.strptime('2024-01-01', '%Y-%m-%d')

    for _ in range(num_transactions):
        date += timedelta(days=1)
        amount = random.randint(100, 5000)
        is_debit = random.choice([True, False])

        if is_debit:
            debit = amount
            credit = 0
            current_balance += debit
        else:
            debit = 0
            credit = amount
            current_balance -= credit

        transactions.append({
            'date': date.strftime('%d %b %Y'),
            'reference': f'REF{random.randint(100000, 999999)}',
            'description': 'Debit Transaction' if is_debit else 'Credit Transaction',
            'valueDate': date.strftime('%d %b %Y'),
            'debit': debit,
            'credit': credit,
            'closingBalance': current_balance
        })

    return transactions

# Find and replace in Excel
def find_and_replace_excel(sheet, replacements):
    for row in sheet.iter_rows():
        for cell in row:
            if isinstance(cell.value, str):
                for to_replace, replace_with in replacements.items():
                    if to_replace in cell.value:
                        cell.value = cell.value.replace(to_replace, replace_with)

# Format date input
def format_date_inp(date_str):
    try:
        parsed_date = datetime.strptime(date_str, '%d %b %Y')
        return parsed_date.strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Date format for {date_str} is not valid.")

# Get current date formatted
def date_printed():
    return datetime.now().strftime('%d %b %Y')

# Get next flight date
def flightnextdate(dater, days):
    return (dater + timedelta(days=days)).strftime("%a %d %B %Y").upper()

# Get next flight day
def flightnextday(dater, days):
    return (dater + timedelta(days=days)).strftime("%d %b").upper()

# Generate flight code
def generate_flight_code():
    return random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=3)) + ''.join(random.choices(string.ascii_uppercase, k=2))

# List of school churches
school_churches = ['Presby', 'Roman Catholic', 'SDA', 'Pentecost', 'Methodist', 'Anglican', 'Baptist', 'Assemblies of God', 'Lutheran', 'Evangelical', 'Charismatic', 'Apostolic']

# Get random school church
def get_school_church():
    return random.choice(school_churches)

# Get Saturday subtracted years
def get_saturday_subtracted_years(years):
    today = date.today()
    while True:
        new_date = today.replace(year=today.year - years)
        if new_date.weekday() == 5:
            return new_date
        
def generate_random_signature(input_string: str) -> str:
    # Remove spaces and ensure input_string is not empty
    input_string = input_string.replace(" ", "")
    if len(input_string) == 0:
        return ""

    # Randomly shuffle the input_string
    shuffled_string = ''.join(random.sample(input_string, len(input_string)))

    return shuffled_string

# Generate random values for marriage
def marryme():
    wit1 = generate_random_name()
    wit11 = generate_random_name()
    wit13 = generate_random_name()
    wit14 = generate_random_name()

    wit2 = generate_random_name()
    wit22 = generate_random_name()
    wit23 = generate_random_name()
    wit24 = generate_random_name()
    values = {
        "licenceno": random.choices(range(10000, 99999), k=4),
        "certno": random.choices(range(10000, 99999), k=4),
        "date": "2024",
        "year": ["2024", "2025", "2026", "2027"],
        "location": ["Ayisi", "Suame", "Medina", "Keta"],
        "marriagecity": ["West Asin", "Kumasi", "Accra", "Ho"],
        "marriageno": ["001", "002", "003", "004"],
        "nameofspouse": ["Alice", "Bob", "Charlie", "Dana"],
        "spousework": ["Engineer", "Doctor", "Teacher", "Artist"],
        "wifeaddress": ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St"],
        "spousefather": [random_male_friend_firstname(), random_male_friend_firstname(), random_male_friend_firstname(), random_male_friend_firstname()],
        "inlawwork": ["Lawyer", "Architect", "Dentist", "Chef"],
        "role": ["Manager", "Developer", "Designer", "Consultant"],
        "myfatherwork": ["Plumber", "Electrician", "Mechanic", "Carpenter"],
        "witness1": [wit1, wit11, wit13, wit14],
        "witness1sig": [generate_random_signature(wit1), generate_random_signature(wit11), generate_random_signature(wit13), generate_random_signature(wit14)],
        "witness2": [wit2, wit22, wit23, wit24],
        "witness2sig": [generate_random_signature(wit2), generate_random_signature(wit22), generate_random_signature(wit23), generate_random_signature(wit24)],
    }
    return {key: random.choice(values[key]) for key in values}

# Make the code faster
make_monday_if_weekend = lambda date_obj: date_obj + timedelta(days=(7 - date_obj.weekday()) % 7) if date_obj.weekday() > 4 else date_obj
subtract_days = lambda days: make_monday_if_weekend(date.today() - timedelta(days=days))
generate_random_trans_id = lambda length: ''.join(random.choices(string.digits, k=length))
generate_random_string = lambda length: ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
formatmydate = lambda today=datetime.now(), formatas="dd/mm/yyyy": today.strftime(formatas)
# objme = lambda date_str: datetime.strptime(date_str, date_format)
number_to_words = lambda num: inflect.engine().number_to_words(num).replace(',', '')
# getplaces = lambda num: random.sample(places[1:], num) if len(places) > num else places[1:]
get_my_farm = lambda: random.choice(datas.land_at)
get_school_church = lambda: random.choice(school_churches)