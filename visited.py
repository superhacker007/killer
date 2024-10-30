import os
from datetime import datetime, timedelta
from flask import request, redirect
from PIL import Image
from PyPDF2 import PdfMerger
import vul, things, emailme, models, bk2, dbconnect, domalta

def create_visitor():
    form = request.form
    files = request.files

    
    conference = form['conference']
    lastname = form['surname']
    firstname = form['firstname']
    destination = form['country']
    city = form['city']
    sex = form['sex']
    dob_str = form['dob']
    dob = vul.datetime.strptime(vul.format_date_inp(dob_str), '%Y-%m-%d')
    ssn = form['ssn']
    passportn = form['passport_number']
    addresss = form['address']
    phonen = form['phonen']
    bn = form['bn']
    acc = form['acc']
    region = form['region']
    branch = form['branch']
    rol = mycity = form['mycity']
    end_date = form['end_date']
    hassal = form['hassal']

    spouse_name = form['spouse']
    spouse_last = form['spouselast']
    child1name = form['child1name']
    child2name = form['child2name']
    fathername = form['fathername']
    fatherlast = form['fatherlast']
    fatherwork = form['fatherwork']
    mothername = form['mothername']
    motherwork = form['motherwork']
    visited = form['visited']
    nationality = form['nationality']

    passport = files.get('passport')

    visitor = models.Visitor(
    firstname=firstname,           # Visitor's first name
    lastname=lastname,             # Visitor's last name
    destination=destination,       # Destination country/city
    city=city,                     # City of residence
    sex=sex,                       # Gender of the visitor
    dob=dob,                       # Date of birth, ensure it's in datetime.date format
    ssn=ssn,                       # Social Security Number
    passportn=passportn,           # Passport number
    addresss=addresss,             # Home address
    phonen=phonen,                 # Phone number
    bn=bn,                         # Business number (if applicable)
    acc=acc,                       # Account number (if applicable)
    region=region,                 # Region of residence
    branch=branch,                 # Branch (if applicable)
    rol=rol,                       # Role or designation (if applicable)
    enddate=end_date,               # End date of the trip (ensure it's a datetime.date object)
    hassal=hassal,                 # Salary information (if applicable)
    nationality=nationality,       # Visitor's nationality
    spouse_name=spouse_name,       # Spouse's first name
    spouse_last=spouse_last,       # Spouse's last name
    child1name=child1name,         # First child's name (if applicable)
    child2name=child2name,         # Second child's name (if applicable)
    fathername=fathername,         # Father's first name
    fatherlast=fatherlast,         # Father's last name
    fatherwork=fatherwork,         # Father's occupation
    mothername=mothername,         # Mother's first name
    motherwork=motherwork,         # Mother's occupation
    visited=visited,               # Countries or places visited
    conference=conference,         # Conference name (if applicable)
    visitor_status='new'  # Status of the visitor (e.g., active, inactive)
)


    models.db.session.add(visitor)
    models.db.session.commit()

    folder_name = f"{visitor.id}_{firstname}_{lastname}".replace(" ","")
    visitor_folder = os.path.join('visitors', folder_name)
    old_file = os.path.join('templates', 'packaging')
    os.makedirs(visitor_folder, exist_ok=True)

    if passport:
        pdf_path = os.path.join(visitor_folder, "passport.pdf")
        file_extension = passport.filename.split('.')[-1].lower()
        if file_extension in ['jpg', 'jpeg', 'png']:
            image = Image.open(passport)
            image.convert('RGB').save(pdf_path)
        else:
            passport.save(pdf_path)

    bankstatement = files.get('bankstatement')
    marriage_cert = files.get('marriage_cert')

    upload_files = {
        "birth_cert": files.get('birth_cert'),
        "child1_cert": files.get('child1_cert'),
        "child2_cert": files.get('child2_cert'),
        "transcript": files.get('transcript'),
        "picture1": files.get('picture1'),
        "picture2": files.get('picture2'),
        "picture3": files.get('picture3'),
        "picture4": files.get('picture4'),
        "picture5": files.get('picture5'),
        "picture6": files.get('picture6'),
    }

    extras = []

    for file_type, file in upload_files.items():
        if file:
            file_extension = file.filename.split('.')[-1].lower()
            pdf_path = os.path.join(visitor_folder, f"{file_type}.pdf")
            try:
                if file_extension in ['jpg', 'jpeg', 'png']:
                    # Convert image to PDF
                    image = Image.open(file)
                    image.convert('RGB').save(pdf_path)
                    extras.append(pdf_path)
                else:
                    file_path = os.path.join(visitor_folder, f"{file_type}.{file_extension}")
                    file.save(file_path)
                    if file_extension == 'pdf':
                        extras.append(file_path)
            except Exception as e:
                print(f"Error processing file {file.filename}: {e}")

    # Merge all PDFs into extras.pdf
    if extras:
        try:
            extras_pdf_path = os.path.join(visitor_folder, 'extras.pdf')
            merger = PdfMerger()
            for pdf in extras:
                merger.append(pdf)
            merger.write(extras_pdf_path)
            merger.close()
            print(f"Extras PDF created at {extras_pdf_path}")
        except Exception as e:
            print(f"Error merging PDFs: {e}")


    attachment_paths = [
        os.path.join(visitor_folder, 'passport.pdf'),
        os.path.join(visitor_folder, 'extras.pdf'),
    ]

    vul.send_email(
         recipient_email="lindahanson@waaptravels.com",
         subject="Bank Statement and Extra Documents",
         body=f"Please find attached documents for {firstname} {lastname}",
         attachment_paths=attachment_paths
    )


    trip_start_date = datetime.strptime(form['start_date'], '%Y-%m-%d')

    if end_date == '':
        enddate_obj = trip_start_date + timedelta(days=7)
    else:
        enddate_obj = datetime.strptime(end_date, '%Y-%m-%d')

    age = vul.syear(datetime.strptime(vul.format_date_inp(dob_str), '%Y-%m-%d'))

    dob = datetime.strptime(vul.format_date_inp(dob_str), '%Y-%m-%d')
    emp_start = datetime.strptime(vul.calculate_employment_start_date_for_daddy(dob) if age < 25 else vul.calculate_employment_start_date(dob), '%Y-%m-%d')
    syear = vul.syear(emp_start)
    current_year = datetime.now().year
    named = vul.generate_random_name()

    if destination == 'australia':
        lian = 'Australian'
        flight = 'flightau'
        flighton = 'FLIGHT EMIRATES 412 - EMIRATES AIRWAYS at 10:15'
        flightnum = '(FLIGHT EMIRATES 415) to Accra scheduled at 06:50 AM'
        reg = 'SYD'
    elif destination == 'canada':
        lian = 'Canadian'
        flight = 'flightca'
        flighton = 'FLIGHT KL 681 - KLM ROYAL DUTCH AIRLINES, 15:55'
        flightnum = '(FLIGHT KL 682) to Accra scheduled at 17:50'
        reg = 'BC'
        invi = 'invi'
        
    elif destination == 'china':
        lian = 'Chinese'
        flight = 'flightca'
        flighton = 'FLIGHT KL 681 - KLM ROYAL DUTCH AIRLINES, 15:55'
        flightnum = '(FLIGHT KL 682) to Accra scheduled at 17:50'
        reg = 'GZ'
    
    elif destination == 'portugal':
        lian = 'Portuguese'
        flight = 'flightca'
        flighton = 'FLIGHT KL 681 - KLM ROYAL DUTCH AIRLINES, 15:55'
        flightnum = '(FLIGHT KL 682) to Accra scheduled at 17:50'
        reg = 'LIS'

    elif destination == 'albania':
        lian = 'Albanian'
        flight = 'flightca'
        flighton = 'FLIGHT KL 681 - KLM ROYAL DUTCH AIRLINES, 15:55'
        flightnum = '(FLIGHT KL 682) to Accra scheduled at 17:50'
        reg = 'BC'
        invi = 'invi'

    if city == 'Toronto':
        reg = 'ON'
        invi = 'torinvi'
        flight = 'flighttor'
        flighton = 'FLIGHT KL 681 - KLM ROYAL DUTCH AIRLINES, 15:55'
        flightnum = '(FLIGHT KL 682) to Accra scheduled at 17:50'


    
    
    mysig = vul.generate_random_signature(lastname).lower()
    fatheremail = ''
    generator = vul.RandomGenerator()

    cover = 'ycover.html' if age < 25 else 'cover.html'
    if age < 25:
        mysig = fatherlast.lower()
        fatheremail = fathername[0].lower() + fatherlast[0].lower() + '@gmail.com'

    mysig = "/Aug"
    sex_data = {'m': (1, 'Mr', 'M', 'him', 'his', 'he'), 'f': (2, 'Ms', 'F', 'her', 'her', 'she')}
    confid, mr, se, him, his, he = sex_data[sex.lower()]

    bank_dict = {
        'om': 'Omnibank',
        'stan': 'Stanbic',
        'nib': 'NIB LTD',
        'adb': 'ADB',
        'gcb': 'GCB LTD',
        'fid': 'Fidelity Bank'
    }
    bank = bank_dict.get(bn, bn)

    network = things.get_network(phonen)
    total_trip_days = 7

    checkin_date = trip_start_date
    days = 7
    nights = days - 1

    if conference == 'yes':
        conferenced = vul.getconference(confid)
        code = conferenced[5]
        mycode = generator.generate_random_numbers(110, 230, 1)[0]
        places = vul.getplaces(3, city)
    else:
        places = vul.getplaces(5, city)
        conferenced = []
        code = ''
        mycode = ''

    staffrand = generator.generate_random_numbers(10, 1000, 1)[0]
    staffrandyear = generator.generate_random_numbers(11, 23, 1)[0]
    staffid = generator.generate_random_numbers(100001, 1000001, 1)[0]
    hotenum = f"{generator.generate_random_numbers(100, 900, 1)[0]}-{generator.generate_random_numbers(1000001, 9000000, 1)[0]}"
    pobx = staffrand // 2

    opb = generator.generate_random_numbers(100000, 190000, 1)[0]
    fdp = generator.generate_random_numbers(10001, 30000, 1)[0]
    hoteref = f"{generator.generate_random_numbers(100, 999, 1)[0]} -{generator.generate_random_numbers(100000, 999999, 1)[0]}"

    random_deep_colors = generator.generate_deep_colors(1)
    if ssn == '':
        vul.ssn

    employer_data = {
        'm': ("Min Of Health", "Ghana Health Service", "GHS", "Lab Technician", "Health", "Korle Bu Teaching Hospital", "Pharmacy", "Health Workers"),
        'f': ("Min Of Health", "Ghana Health Service", "GHS", "Nurse", "Health", "Korle Bu Teaching Hospital", "Nurse", "Health Workers"),
        # 'm': ("Min Of Education", "Ghana Education Service", "GES", "Teacher", "Teacher", "Accra High", "Teacher", "Teachers"),
        # 'm': ("Min Of Education", "Ghana Education Service", "GES", "Teacher", "Teacher", "Accra High", "Teacher", "Teachers"),
    }
    min, employer, dept, work, typer, school, studied, retention = employer_data[sex.lower()]

    cost = dept

    friend = vul.random.choice(vul.datas.friends_list)
    previous_travel = vul.previous_travel()
    email = f"{firstname} {lastname}{dob.strftime('%Y')}@gmail.com"

    # day_ind, month_name, year_last_two, year_last_two_word = vul.extract_date_parts(19,5)
    # depday1, depmon1 = vul.get_day_and_month(trip_start_date,0)
    # arday1, armon1 = vul.get_day_and_month(trip_start_date,1)
    # depday2, depmon2 = vul.get_day_and_month(trip_start_date,1)
    # arday2, armon2 = vul.get_day_and_month(trip_start_date,1)
    # renday1, renmonth1 = vul.get_day_and_month(enddate_obj,0)
    # renarday1, renarmonth1 = vul.get_day_and_month(enddate_obj,1)
    # renday2, renmonth2 = vul.get_day_and_month(enddate_obj,1)
    # renarday2, renarmonth2 = vul.get_day_and_month(enddate_obj,1)
    dater_start, ourreflev, ourrefmonlev = vul.process_date(trip_start_date)
    dater_end, _, _ = vul.process_date(enddate_obj)
    dater_emp_start, ourrefemp, ourrefmon = vul.process_date(emp_start)
    leaveletterdate, _, _ = vul.process_date(vul.subtract_days(5))


    

    document_filenames = ['studentid', 'empletter', 'levletter', 'visitintro', 'appointment', 'fathersponsor', 'reference', 'marriage', 'bud', 'ite', 'om', 'inde', 'hote', 'invi', 'flight', 'payslip', 'jan', 'feb', 'mar', 'apr', 'may', 'jun','jul', 'intro', 'personal', 'stats', 'cover', 'stan', 'farm','church']
    document_paths = {filename: vul.get_document_paths(visitor_folder, filename) for filename in document_filenames}

    options = {
        'no-pdf-compression': None,
        'disable-javascript': None,
        'enable-local-file-access': True,
    }

    if bankstatement.filename != '':
        bankstatement.save(os.path.join(visitor_folder, 'bankstatement.pdf'))
        anualsal = float(form['salary'])*12
    else:
        anualsal = round(vul.random.uniform(60000, 70000), 2)
    
    monthly_values = [(anualsal/12) * i for i in range(1, 7)]
    ytd_values = {f"ytdgrosspay{i+1}": monthly_values[i] for i in range(6)}
    mgross = anualsal / 12
    sscemp = 0.055 * mgross
    ytdssfworker_values = {f"ytdssfworker{i+1}": sscemp * (i + 1) for i in range(6)}
    incometax = mgross * 0.135
    ytdincometax_values = {f"ytdincometax{i+1}": incometax * (i + 1) for i in range(6)}
    monthlyssf = 0.13 * mgross
    ytdssf_values = {f"ytdssf{i+1}": monthlyssf * (i + 1) for i in range(6)}
    monsal = mgross
    premium = generator.generate_random_numbers(500, 1000, 1)[0]
    bonus = generator.generate_random_numbers(400, 900, 1)[0]
    union1 = int(generator.generate_random_numbers(60, 100, 1)[0])
    union2 = int(generator.generate_random_numbers(60, 100, 1)[0])
    union3 = int(generator.generate_random_numbers(60, 100, 1)[0])
    siclife = int(generator.generate_random_numbers(60, 100, 1)[0])

    tpayments = monsal + premium + bonus
    tdeduct = sscemp + incometax + union1 + union2 + siclife + union3
    sal = tpayments - tdeduct
    if bankstatement.filename != '':
        sal = float(form['salary'])

    thehotel = vul.gethotel(city)
    land_price = round(vul.random.randint(100, 500) * 1000)
    daybought, monthbought, yearbought = vul.format_date_with_suffix_split(vul.subtract_years_months(syear, 7))
    ddaybought, dmonthbought, dyearbought = vul.format_date_with_suffix_split(vul.subtract_years_months(syear, 6))
    daymar, monthmar, yearmar = vul.format_date_with_suffix_split(vul.subtract_years_months(syear, 5))
    landlord = vul.generate_random_name()
    postedto = vul.get_school_church() + ' secondary school'
    profirst = vul.random.choice(vul.datas.first_male_names)
    proflast = vul.random.choice(vul.datas.last_names)
    geoloc = vul.random.randint(30, 90)
    clean_firstname = firstname.replace(' ', '').replace('-', '').lower()
    clean_lastname = lastname.replace(' ', '').replace('-', '').lower()
    email2 = clean_firstname+clean_lastname+str(vul.random.randint(1, 100))
    emailme.create_email(email2, email,"linda@workgh.com")
    email2all = email2 + '@workgh.com'
    template_vars_common = {
        'lastname': lastname,
        'firstname': firstname,
        'sex': sex,
        'mr': mr,
        'se': se,
        'him': him,
        'his': his,
        'he': he,
        'rol': rol,
        'retention': retention,
        'age': age,
        'syear': syear,
        'current_year': current_year,
        'named': named,
        'startdate': trip_start_date,
        'days': days,
        'nights': nights,
        'dob': dob,
        'passportn': passportn,
        'myaddress': addresss,
        'phonen': phonen,
        'mycity': mycity,
        'email': email,
        'role': work,
        'branch': branch,
        'bn': bn,
        'acc': acc,
        'ssn': ssn,
        'region': region,
        'district': branch,
        'staffid': staffid,
        'unitcode': staffid // 200,
        'sal': sal,
        'min': min,
        'dept': dept,
        'work': work,
        'unionlab1': 'GRNMA Welfare and Devt Levy' if sex == 'm' else 'NAGRAT Welfare and Devt Levy',
        'unionlab2': 'GH Registered Health Workers Dues' if sex == 'm' else 'GH Registered Teachers Dues',
        'unionlab3': 'Health Union Dues' if sex == 'm' else 'Teachers Union Dues',
        'typer': typer,
        'thehotel': thehotel[1][1],
        'employer': employer,
        'school': school,
        'studied': studied,
        'network': network,
        'acres': vul.random.randint(5, 20),
        'landprice': "{:,.2f}".format(land_price),
        'landpriceinwords': things.convert_amount_to_words(land_price),
        'landdeposit': "{:,.2f}".format(land_price / 10),
        'monthbought': monthbought,
        'daybought': daybought,
        'yearbought': str(yearbought)[-2:],
        'dmonthbought': dmonthbought,
        'ddaybought': ddaybought,
        'dyearbought': str(dyearbought)[-2:],
        'farmcity': vul.get_my_farm(),
        'selleraddress': vul.get_my_farm(),
        'pobx': pobx,
        'landlord': landlord,
        'mysig': mysig,
        'sellersign': landlord[3:],
        'spouse_name': spouse_name,
        'spouse_last': spouse_last,
        'wifesig': vul.generate_random_signature(spouse_name),
        'postedto': postedto,
        'schooladd': postedto,
        'schoolphone': f'030{vul.random.randint(1000000, 9999999)}',
        'headmasterphone': f'024{vul.random.randint(1000000, 9999999)}',
        'headmaster': vul.generate_random_name(),
        'schoolemail': f'info@{postedto.replace(" ", "").lower()}.com',
        'emp_year': emp_start.strftime('%Y'),
        'profirst': profirst,
        'proflast': proflast,
        'promid': 'K',
        'fathername': fathername,
        'fatherlast': fatherlast,
        'fatherwork': fatherwork,
        'fathersig': mysig,
        'appointment_date': vul.add_day_and_format(enddate_obj, 35),
        'city': city,
        'gooddate': vul.add_day_and_format(vul.datetime.now(), -35),
        'profemail': f'prof{profirst.lower()}{proflast.lower()}',
        'fatheremail': fatheremail,
        'conference': conference,
        'conferenced': conferenced,
        'mothername': mothername,
        'motherwork': motherwork,
        'conference': conference,
        'daymar': daymar,
        'monthmar': monthmar,
        'yearmar': str(yearmar)[-2:],
        'geoloc': geoloc,
        'visited': visited,
        'child1name': child1name,
        'child2name': child2name,
        'email2all': email2all,
        'reg': reg,
        'lian': lian,
        'flighton': flighton,
        'flightnum': flightnum,
        'destination': destination,
        'hassal': hassal,
    }

    transactions = []
    summary = []
    chunks = []
    top_date = ''
    stamp_date = ''

    if destination == 'malta':
        return domalta.MaltaAutomation.digital_malt(template_vars_common)


    if age > 25 or bn != 'om':
        if bankstatement.filename != '':
            print('Saved bank statement')
        else:
            end_date = vul.datetime.now().strftime("%Y-%m-%d")
            if destination == 'japan':
                initial_balance = round(vul.random.uniform(50000, 70000), 2)
            else:
                initial_balance = round(vul.random.uniform(320000, 500000), 2)

            if bn == 'adb':
                start = 25
                continue_from = 38
                transactions, summary = bk2.generate_random_transactions_adb(template_vars_common, initial_balance, sal)
            elif bn == 'stan':
                start = 9
                continue_from = 18
                transactions, summary = bk2.generate_random_transactions(template_vars_common, initial_balance, sal)
            elif bn == 'gcb':
                start = 17
                continue_from = 28
                initial_balance = round(vul.random.uniform(420000, 500000), 2)
                transactions, summary = bk2.generate_random_transactions_gcb(template_vars_common, initial_balance, sal)
            elif bn == 'nib':
                start = 10
                continue_from = 10
                initial_balance = round(vul.random.uniform(420000, 550000), 2)
                transactions, summary = bk2.generate_random_transactions_nib(template_vars_common, initial_balance, sal)
            
            
            last_transaction_date = vul.objme(summary['last_transaction_date'])
            top_date = vul.formatmydate(last_transaction_date, ("%d %B %Y"))
            stamp_date = vul.formatmydate(last_transaction_date, ("%d/%m/%Y"))

            first_page_transactions = transactions[:start]
            subsequent_page_transactions = transactions[start:]
            chunks = [first_page_transactions] + [subsequent_page_transactions[i:i+continue_from] for i in range(0, len(subsequent_page_transactions), continue_from)]

            
    marryme = vul.marryme()
    pdf_files = []

    vul.render_html_to_pdf('/packaging/hote.html', os.path.join(visitor_folder, 'hote.html'), document_paths['hote'][1], {**template_vars_common, 'startdate': vul.get_formatted_date(trip_start_date), 'enddfhoteate': vul.get_formatted_date(enddate_obj), 'destination': thehotel[1][0], 'hotelname': thehotel[1][1],'hoteladd': thehotel[1][2],'hotesub': thehotel[1][3], 'hotell': thehotel[1][4],'hotelfax': thehotel[1][5], 'fordate': vul.get_formatted_date(),'available':vul.subtract_month_and_format(trip_start_date), 'hotenum': hotenum, 'hoteref': hoteref, 'generated_on':vul.get_formatted_date(vul.datetime.now()), 'geoloc':geoloc, 'stars':thehotel[1][6]}, options)

    vul.render_html_to_pdf(f'/packaging/{flight}.html', os.path.join(visitor_folder, 'flight.html'), document_paths['flight'][1], {**template_vars_common, 'takeoff_date': vul.flightnextdate(trip_start_date,0), 'takeoff_day':vul.flightnextday(trip_start_date,0) , 'trans':vul.flightnextday(trip_start_date,1), 'transdate1':vul.flightnextdate(trip_start_date,1), 'comback_takeoff': vul.flightnextdate(enddate_obj,0), 'comback1':vul.flightnextday(enddate_obj,0) , 'combackplus1day':vul.flightnextday(enddate_obj,1), 'comebacktrans':vul.flightnextdate(enddate_obj,1) ,'flightcode': vul.generate_flight_code(), 'issued': vul.datetime.now().strftime("%d %B %Y").upper() }, options)

    vul.render_html_to_pdf('/packaging/bud.html', os.path.join(visitor_folder, 'bud.html'), document_paths['bud'][1], {**template_vars_common, 'startdate':vul.day_with_suffix(trip_start_date), 'enddate':dater_end, 'destination':destination.upper()}, options)

    vul.render_html_to_pdf('/packaging/ite.html', os.path.join(visitor_folder, 'ite.html'), document_paths['ite'][1], {**template_vars_common, 'ites':places, 'total_trip_days': total_trip_days, 'city':city, 'start_date_trip':trip_start_date, 'end_date_trip':enddate_obj, 'deep': random_deep_colors[0]}, options)

    if age > 25:
        if bankstatement.filename == '':
            vul.render_html_to_file(f'/packaging/{bn}.html', os.path.join(visitor_folder, 'stan.html'), {**template_vars_common, 'transactions':transactions,'chunks':chunks, 'summary':summary, 'top_date':top_date, 'stamp_date':stamp_date, 'towords':things.convert_amount_to_words(float(summary['closing_balance'].replace(',',''))), 'openedon': vul.add_day_and_format(emp_start,50)}, options)

        if marriage_cert is not None:
            marriage_cert.save(os.path.join(visitor_folder, 'marriage.pdf'))
        else:
            vul.render_html_to_file('/packaging/marriage.html', os.path.join(visitor_folder, 'marriage.html'), {**template_vars_common, 'marryme':marryme}, options)

        vul.render_html_to_pdf(f'/packaging/flevletter.html', os.path.join(visitor_folder, 'levletter.html'), document_paths['levletter'][1], {**template_vars_common, 'staffid': staffid, 'staffrand': staffrand, 'staffrandyear': staffrandyear, 'leaveletterdate': leaveletterdate, 'ourreflev': ourreflev, 'ourrefmonlev': ourrefmonlev, 'start_date':vul.day_with_suffix(trip_start_date)}, options)

        vul.render_html_to_pdf(f'/packaging/fvisitintro.html', os.path.join(visitor_folder, 'visitintro.html'), document_paths['visitintro'][1], {**template_vars_common, 'staffid': staffid, 'staffrand': staffrand, 'staffrandyear': staffrandyear, 'leaveletterdate': leaveletterdate, 'ourreflev': ourreflev, 'ourrefmonlev': ourrefmonlev, 'start_date':vul.day_with_suffix(trip_start_date), 'stamp_date':stamp_date, 'cost':cost}, options)

        vul.render_html_to_pdf(f'/packaging/church.html', os.path.join(visitor_folder, 'church.html'), document_paths['church'][1], {**template_vars_common, 'stamp_date':stamp_date}, options)
        

        vul.render_html_to_pdf('/packaging/farm.html', os.path.join(visitor_folder, 'farm.html'), document_paths['farm'][1], {**template_vars_common, 'staffid': staffid, 'staffrand': staffrand, 'staffrandyear': staffrandyear, 'leaveletterdate': leaveletterdate, 'ourreflev': ourreflev, 'ourrefmonlev': ourrefmonlev, 'start_date':vul.day_with_suffix(trip_start_date)}, options)

        vul.render_html_to_pdf(f'/packaging/fempletter.html', os.path.join(visitor_folder, 'empletter.html'), document_paths['empletter'][1], {**template_vars_common, 'emp_start_date': dater_emp_start, 'ourrefemp': ourrefemp, 'ourrefmon': ourrefmon}, options)

        month_templates = ['feb', 'mar', 'apr', 'may', 'jun', 'jul']
        for i, month in enumerate(month_templates, 1):
            vul.render_html_to_pdf(f'/packaging/{month}.html', os.path.join(visitor_folder, f'{month}.html'), document_paths[month][1], {**template_vars_common, 'branch':branch, 'bank': bank, 'ytdssf':"{:,.2f}".format(ytdssf_values[f'ytdssf{i}']), 'monthlyssf':"{:,.2f}".format(monthlyssf), 'ytdincometax':"{:,.2f}".format(ytdincometax_values[f'ytdincometax{i}']), 'mgross':"{:,.2f}".format(mgross), 'ytdgrosspay':"{:,.2f}".format(ytd_values[f'ytdgrosspay{i}']), 'anualsal': "{:,.2f}".format(anualsal),'union3':"{:,.2f}".format(union3), 'siclife':"{:,.2f}".format(siclife), 'union2': "{:,.2f}".format(union2), 'union1':"{:,.2f}".format(union1), 'incometax': "{:,.2f}".format(incometax),'sscemp':"{:,.2f}".format(sscemp), 'cost':cost, 'bonus': "{:,.2f}".format(bonus), 'premium': "{:,.2f}".format(premium), 'monsal':"{:,.2f}".format(monsal), 'tpayments': "{:,.2f}".format(tpayments),'tdeduct':"{:,.2f}".format(tdeduct),'ytdssfworker': "{:,.2f}".format(ytdssfworker_values[f'ytdssfworker{i}']), 'salary':"{:,.2f}".format(sal)}, options)

        vul.render_html_to_pdf('/packaging/appointment.html', os.path.join(visitor_folder, 'appointment.html'), document_paths['appointment'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y")}, options)

        if conference == 'yes':
            vul.render_html_to_pdf(f'/packaging/{invi}.html', os.path.join(visitor_folder, 'invi.html'), document_paths['invi'][1], {**template_vars_common, 'code': code, 'mycode': mycode, 'issuedate': vul.format_date_to_month_day(), 'mydob': vul.format_my_day(dob), 'name': conferenced[0], 'venue': conferenced[2], 'address': conferenced[3], 'heldon': conferenced[6], 'senton': conferenced[7], 'unitcode': str(staffid // 200)}, options)
            vul.render_html_to_pdf('/packaging/concover.html', os.path.join(visitor_folder, 'cover.html'), document_paths['cover'][1], {**template_vars_common,'ites':places,'dob':vul.day_with_suffix(dob), 'date1': vul.flightnextdate(trip_start_date,1), 'date2': vul.flightnextdate(trip_start_date,2), 'date3': vul.flightnextdate(trip_start_date,3), 'date4': vul.flightnextdate(trip_start_date,4), 'date5': vul.flightnextdate(trip_start_date,5), 'date6': vul.flightnextdate(trip_start_date,6), 'date7': vul.flightnextdate(trip_start_date,7), 'friend':friend, 'previous': previous_travel, 'joinback':vul.flightnextdate(enddate_obj,8), 'appointment1':vul.flightnextdate(enddate_obj,18), 'appointment2':vul.flightnextdate(enddate_obj,30), 'conferenced':conferenced}, options)
            pdf_files2 = [os.path.join(visitor_folder, f'{doc}.pdf') for doc in ['cover', 'levletter', 'visitintro', 'appointment', 'ite', 'hote', 'flight', 'bud']]
        else:
            vul.render_html_to_pdf(f'/packaging/{cover}', os.path.join(visitor_folder, 'cover.html'), document_paths['cover'][1], {**template_vars_common, 'ites':places, 'dob':vul.day_with_suffix(dob), 'date1': vul.flightnextdate(trip_start_date, 1), 'date2': vul.flightnextdate(trip_start_date, 2), 'date3': vul.flightnextdate(trip_start_date, 3), 'date4': vul.flightnextdate(trip_start_date, 4), 'date5': vul.flightnextdate(trip_start_date, 5), 'date6': vul.flightnextdate(trip_start_date, 6), 'date7': vul.flightnextdate(trip_start_date, 7), 'friend':friend, 'previous': previous_travel, 'joinback':vul.flightnextdate(enddate_obj, 8), 'appointment1':vul.flightnextdate(enddate_obj, 18), 'appointment2':vul.flightnextdate(enddate_obj, 30)}, options)
            pdf_files2 = [os.path.join(visitor_folder, f'{doc}.pdf') for doc in ['cover', 'visitintro', 'ite', 'hote', 'flight', 'bud', 'appointment']]

        if bankstatement.filename != '':
            pdf_files = ['bankstatement.pdf','empletter.pdf', 'feb.pdf', 'mar.pdf', 'apr.pdf', 'may.pdf', 'farm.pdf']
        else:
            pdf_files = ['empletter.pdf', 'feb.pdf', 'mar.pdf', 'apr.pdf', 'may.pdf', 'farm.pdf']

    else:
        if bn != 'om':
            vul.render_html_to_pdf(f'/packaging/{bn}.html', os.path.join(visitor_folder, 'stan.html'), {**template_vars_common, 'transactions':transactions, 'chunks':chunks, 'summary':summary, 'top_date':top_date, 'stamp_date':stamp_date, 'firstname':fathername, 'lastname':fatherlast, 'toson': 200000}, options)

        vul.render_html_to_file(f'/packaging/{form["bn2"]}.html', os.path.join(visitor_folder, 'mybank.html'), {**template_vars_common, 'transactions':transactions, 'chunks':chunks, 'summary':summary, 'top_date':top_date, 'stamp_date':stamp_date, 'toson': 200000}, options)

        vul.render_html_to_pdf('/packaging/fathersponsor.html', os.path.join(visitor_folder, 'fathersponsor.html'), document_paths['fathersponsor'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y")}, options)
        vul.render_html_to_pdf('/packaging/studentid.html', os.path.join(visitor_folder, 'studentid.html'), document_paths['studentid'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y")}, options)
        vul.render_html_to_pdf('/packaging/appointment.html', os.path.join(visitor_folder, 'appointment.html'), document_paths['appointment'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y")}, options)
        vul.render_html_to_pdf('/packaging/reference.html', os.path.join(visitor_folder, 'reference.html'), document_paths['reference'][1], {**template_vars_common}, options)
        vul.render_html_to_pdf('/packaging/farm.html', os.path.join(visitor_folder, 'farm.html'), document_paths['farm'][1], {**template_vars_common, 'staffid': staffid, 'staffrand': staffrand, 'staffrandyear': staffrandyear, 'leaveletterdate': leaveletterdate, 'ourreflev': ourreflev, 'ourrefmonlev': ourrefmonlev, 'start_date':vul.day_with_suffix(trip_start_date), 'firstname':fathername, 'lastname':fatherlast}, options)
        vul.render_html_to_pdf(f'/packaging/fempletter.html', os.path.join(visitor_folder, 'empletter.html'), document_paths['empletter'][1], {**template_vars_common, 'emp_start_date': dater_emp_start, 'ourrefemp': ourrefemp, 'ourrefmon': ourrefmon, 'firstname':fathername, 'lastname':fatherlast}, options)

        month_templates = ['mar', 'apr', 'may', 'jun','jul']
        for i, month in enumerate(month_templates, 3):
            vul.render_html_to_pdf(f'/packaging/{month}.html', os.path.join(visitor_folder, f'{month}.html'), document_paths[month][1], {**template_vars_common, 'branch': branch, 'bank': bank, 'ytdssf': "{:,.2f}".format(ytdssf_values[f'ytdssf{i}']), 'monthlyssf': "{:,.2f}".format(monthlyssf), 'ytdincometax': "{:,.2f}".format(ytdincometax_values[f'ytdincometax{i}']), 'mgross': "{:,.2f}".format(mgross), 'ytdgrosspay': "{:,.2f}".format(ytd_values[f'ytdgrosspay{i}']), 'anualsal': "{:,.2f}".format(anualsal), 'union3': "{:,.2f}".format(union3), 'siclife': "{:,.2f}".format(siclife), 'union2': "{:,.2f}".format(union2), 'union1': "{:,.2f}".format(union1), 'incometax': "{:,.2f}".format(incometax), 'sscemp': "{:,.2f}".format(sscemp), 'cost': cost, 'bonus': "{:,.2f}".format(bonus), 'premium': "{:,.2f}".format(premium), 'monsal': "{:,.2f}".format(monsal), 'tpayments': "{:,.2f}".format(tpayments), 'tdeduct': "{:,.2f}".format(tdeduct), 'ytdssfworker': "{:,.2f}".format(ytdssfworker_values[f'ytdssfworker{i}']), 'salary': "{:,.2f}".format(sal), 'firstname': fathername.upper(), 'lastname': fatherlast.upper()}, options)

        if conference == 'yes':
            vul.render_html_to_pdf('/packaging/invi.html', os.path.join(visitor_folder, 'invi.html'), document_paths['invi'][1], {**template_vars_common, 'code': code, 'mycode': mycode, 'issuedate': vul.format_date_to_month_day(), 'mydob': vul.format_my_day(dob), 'name': conferenced[0], 'venue': conferenced[2], 'address': conferenced[3], 'heldon': conferenced[6], 'senton': conferenced[7], 'unitcode': str(staffid // 200)}, options)
            vul.render_html_to_pdf('/packaging/concover.html', os.path.join(visitor_folder, 'cover.html'), document_paths['cover'][1], {**template_vars_common, 'ites': places, 'dob': vul.day_with_suffix(dob), 'date1': vul.flightnextdate(trip_start_date, 1), 'date2': vul.flightnextdate(trip_start_date, 2), 'date3': vul.flightnextdate(trip_start_date, 3), 'date4': vul.flightnextdate(trip_start_date, 4), 'date5': vul.flightnextdate(trip_start_date, 5), 'date6': vul.flightnextdate(trip_start_date, 6), 'date7': vul.flightnextdate(trip_start_date, 7), 'friend': friend, 'previous': previous_travel, 'joinback': vul.flightnextdate(enddate_obj, 8), 'appointment1': vul.flightnextdate(enddate_obj, 18), 'appointment2': vul.flightnextdate(enddate_obj, 30), 'conferenced': conferenced}, options)
            pdf_files2 = [os.path.join(visitor_folder, f'{doc}.pdf') for doc in ['cover', 'invi', 'ite', 'hote', 'flight', 'bud', 'reference', 'studentid', 'appointment']]
        else:
            vul.render_html_to_pdf(f'/packaging/{cover}', os.path.join(visitor_folder, 'cover.html'), document_paths['cover'][1], {**template_vars_common, 'ites': places, 'dob': vul.day_with_suffix(dob), 'date1': vul.flightnextdate(trip_start_date, 1), 'date2': vul.flightnextdate(trip_start_date, 2), 'date3': vul.flightnextdate(trip_start_date, 3), 'date4': vul.flightnextdate(trip_start_date, 4), 'date5': vul.flightnextdate(trip_start_date, 5), 'date6': vul.flightnextdate(trip_start_date, 6), 'date7': vul.flightnextdate(trip_start_date, 7), 'friend': friend, 'previous': previous_travel, 'joinback': vul.flightnextdate(enddate_obj, 8), 'appointment1': vul.flightnextdate(enddate_obj, 18), 'appointment2': vul.flightnextdate(enddate_obj, 30), 'conferenced': conferenced}, options)
            pdf_files2 = [os.path.join(visitor_folder, f'{doc}.pdf') for doc in ['cover', 'ite', 'hote', 'flight', 'bud', 'reference', 'studentid', 'appointment', extras]]

        pdf_files = ['fathersponsor.pdf', 'empletter.pdf', 'mar.pdf', 'apr.pdf', 'may.pdf', 'jun.pdf', 'farm.pdf']

    output_pdf = 'merged_output.pdf'
    vul.merge_pdfs(visitor_folder, pdf_files, output_pdf)

    output_pdf2 = 'travel_purpose.pdf'
    merged_pdf_path = vul.merge_diff_pdfs(pdf_files2, visitor_folder, output_pdf2)
    
    templates_folder = os.path.abspath('templates/packaging')

    # Example usage
    pdf_files3 = [
        os.path.join(visitor_folder,'invi.pdf'),
        os.path.join(templates_folder, 'invi1.pdf') 
    ]

    # Output PDF file name
    output_pdf3 = 'invitation.pdf'

    # Merge PDFs
    if conference == 'yes':
        merged_pdf_path3 = vul.merge_diff_pdfs(pdf_files3, visitor_folder, output_pdf3)

    if destination == 'australia':
        # previous_travel_files = [
        #     os.path.join(visitor_folder,'picture1.pdf'),
        # ]

        # previous_travel_output = 'previous_travel.pdf'
        if marriage_cert is not None:
            planned_travel_files = [
                'cover.pdf','church.pdf','ite.pdf','hote.pdf','flight.pdf','bud.pdf','appointment.pdf','marriage.pdf','extradocs.pdf'
            ]
        else:
            planned_travel_files = [
                'cover.pdf','church.pdf','ite.pdf','hote.pdf','flight.pdf','bud.pdf','appointment.pdf','extras.pdf'
            ]

        planned_travel_output = destination+'planned_travel.pdf'

        
        employment_files = [
            'visitintro.pdf','empletter.pdf','levletter.pdf','mar.pdf','apr.pdf','may.pdf','jun.pdf','jul.pdf'
        ]
        

        employment_output = destination+'_employment.pdf'

        if bankstatement.filename != '':
            proof_of_funds_files = [
            'bankstatement.pdf', 'farm.pdf'
            ]

            proof_of_funds_output = destination+'_proof_of_funds.pdf'

            vul.merge_pdfs(visitor_folder, proof_of_funds_files, proof_of_funds_output)

        # vul.merge_diff_pdfs(visitor_folder, previous_travel_files, previous_travel_output)

        vul.merge_pdfs(visitor_folder, planned_travel_files, planned_travel_output)

        vul.merge_pdfs(visitor_folder, employment_files, employment_output)



    vul.compress_pdf_last(os.path.join(visitor_folder, 'travel_purpose.pdf'), os.path.join(visitor_folder, 'extradocs.pdf'))
    vul.compress_pdf(os.path.join(visitor_folder, 'merged_output.pdf'), os.path.join(visitor_folder, 'bank_statement.pdf'))

    attachment_paths = [
        os.path.join(visitor_folder, 'bank_statement.pdf'),
        os.path.join(visitor_folder, 'extradocs.pdf'),
    ]

    if conference == 'yes':
        data = {
            "firstname": firstname,
            "lastname": lastname,
            "code": f"{code}-{mycode}",
            "passport": passportn,
            "country": "Ghana",
        }

        dbconnect.insert_into_table(
            host="globalconference.cc",
            database="u131128410_crazy",
            user="u131128410_crazycode",
            password="CrazyCoder@2024",
            table="persons",
            data=data
        )

    vul.send_email(
         recipient_email="lindahanson@waaptravels.com",
         subject="Bank Statement and Extra Documents",
         body=f"Please find attached documents for {firstname} {lastname} {email2all}",
         attachment_paths=attachment_paths
    )

    return 'done'
