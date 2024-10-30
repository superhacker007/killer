import sul, vul, bk2, things, emailme, models, os, cvsop,schooldatas, time

import requests

def gen_student():
    API_URL = "http://127.0.0.1:5000/studentsapi"

    def update_student_status(student_id, new_status):
        # API endpoint for updating student status
        update_url = f"{API_URL}/update/{student_id}"

        # Data to be updated
        update_data = {
            "student_status": new_status
        }

        # Send PATCH request to update the student status
        response = requests.patch(update_url, json=update_data)

        if response.status_code == 200:
            print(f"Successfully updated student status to '{new_status}' for student ID {student_id}")
        else:
            print(f"Failed to update status for student ID {student_id}. Status Code: {response.status_code}")

    def do_student(studented):
        form = studented
        lastname = form['lastname']
        firstname = form['firstname']
        sex = form['sex']
        dob_str = form['dob']
        ssn = form['ssn']
        passportn = form['passportn']
        dob = vul.datetime.strptime(vul.format_date_inp(form['dob']), '%Y-%m-%d')
        dob = form['dob']
        addresss = form['address']
        phonen = form['phonen']
        email = form['email']
        bn = form['bn']
        acc = form['acc']
        region = form['region']
        branch = form['branch']
        rol = mycity = form['mycity']
        nationality =  form['nationality']
        employer = form['employer']
        role = form['role']
        course = form['course']
        university = form['university']
        gradyear = form['gradyear']
        myclass = form['myclass']
        fromcountry = form['fromcountry']
        destination = form['destination']
        tostudy = form['tostudy']
        cv=form['cv']

        network = things.get_network(phonen)
        current_year = vul.datetime.now().year
        named = vul.generate_random_name()

        dob = vul.datetime.strptime(vul.format_date_inp(dob_str), '%Y-%m-%d')

        generator = vul.RandomGenerator()

        if acc == '':
            acc = generator.generate_random_numbers(200000001, 299999999, 1)[0]
        
        
        staffrand = generator.generate_random_numbers(10, 1000, 1)[0]
        indwrite = generator.generate_random_numbers(2, 47, 1)[0]
        staffrandyear = generator.generate_random_numbers(11, 23, 1)[0]
        staffid = generator.generate_random_numbers(100001, 1000001, 1)[0]
        hotenum = str(generator.generate_random_numbers(100, 900, 1)[0]) + '-' + str(generator.generate_random_numbers(1000001, 9000000, 1)[0])
        filghtbooking = staffid*2
        hotelbooking = staffid/3
        pobx = int(staffrand/2)

        opb = generator.generate_random_numbers(100000, 190000, 1)[0]
        fdp = generator.generate_random_numbers(10001, 30000, 1)[0]
        hoteref = str (generator.generate_random_numbers(100, 999, 1)[0]) + ' -' + str(generator.generate_random_numbers(100000, 999999, 1)[0])
        staffid = staffid



        random_deep_colors = generator.generate_deep_colors(1)

        if destination == 'australia':
            lian = 'Australian'
            
        elif destination == 'canada':
            lian = 'Canadian'
            

        elif destination == 'uk':
            lian = 'British'
            

        if ssn == '':
            vul.ssn
        
        if sex == 'm':
            mr = 'Mr'
            se = 'M'
            him = 'him'
            his = 'his'
            he = 'he'
        else:
            mr = 'Ms'
            se = 'F'
            him = 'her'
            his = 'her'
            he = 'she'

        if sex  == 'f':
            min = "Min Of Health"
            dept = "GHS"
            role = work = "Pharmacist"
            unionlab1 = "GRNMA Welfare and Devt Levy"
            unionlab2 = "GH Registered Health Workers Dues"
            unionlab3 = "Health Union Dues"
            typer = "Health"
            cost = "GHS"
            retention = 'Health Workers'
        else:
            min = "Min Of Education"
            dept = "GES"
            role = work = "Teacher"
            unionlab1 = "NAGRAT Welfare and Devt Levy"
            unionlab2 = "GH Registered Teachers Dues"
            unionlab3 = "Teachers Union Dues"
            typer = "Health"
            cost = "GHS"
            retention = 'Teachers'

        age = vul.syear(vul.datetime.strptime(vul.format_date_inp(dob_str), '%Y-%m-%d'))

        emp_start = vul.datetime.strptime(vul.calculate_employment_start_date_for_daddy(dob) if age < 25 else vul.calculate_employment_start_date(dob), '%Y-%m-%d')
        syear = vul.syear(emp_start)
        current_year = vul.datetime.now().year
        
        # Create a folder for the Student
        folder_name = str(form['id']) + '_' + firstname + '_' + lastname
        student_folder = os.path.join('students', folder_name)
        os.makedirs(student_folder, exist_ok=True)

        # Define document base filenames
        document_filenames = ['cv','credit','poststudy','personal','stats','mar','apr','may','jun','jul','stan','sponsorme','ukstudycover','legonref','sop1','sop2','sop3','sop_1','sop_2','sop_3','sop__1','sop__2','sop__3','sop__4','sop__5','profi','invoice']

        # Generate paths for each document
        document_paths = {filename: vul.get_document_paths(student_folder, filename) for filename in document_filenames}

        # Now, document_paths is a dictionary where keys are base filenames
        # and values are tuples containing the HTML and PDF paths
        # For example, to access the empletter paths:


        options = {
        'no-pdf-compression': None,
        'disable-javascript': None,
        'enable-local-file-access': True,  # Allow wkhtmltopdf to access local files

        # For SSL/TLS issues, the below options might not work as expected in all versions
        # 'no-check-certificate': None,  # This is the line causing the issue
        'ssl-crt-path': None  # This is a placeholder; there's no direct wkhtmltopdf option to ignore SSL errors
        }

        anualsal = round(vul.random.uniform(45000, 49000), 2)
        ytdgrosspay = (float(anualsal)/12)*1
        ytdgrosspay2 = (float(anualsal)/12)*2
        ytdgrosspay3 = (float(anualsal)/12)*3
        ytdgrosspay4 = (float(anualsal)/12)*4
        ytdgrosspay5 = (float(anualsal)/12)*5
        ytdgrosspay6 = (float(anualsal)/12)*6
        ytdgrosspay7 = (float(anualsal)/12)*7
        mgross = anualsal/12
        sscemp = 0.055*mgross
        ytdssfworker = (sscemp)*1
        ytdssfworker2 = (sscemp)*2
        ytdssfworker3 = (sscemp)*3
        ytdssfworker4 = (sscemp)*4
        ytdssfworker5 = (sscemp)*5
        ytdssfworker6 = (sscemp)*6
        ytdssfworker7 = (sscemp)*7
        incometax = mgross*0.135
        ytdincometax = (incometax)*1
        ytdincometax2 = (incometax)*2
        ytdincometax3 = (incometax)*3
        ytdincometax4 = (incometax)*4
        ytdincometax5 = (incometax)*5
        ytdincometax6 = (incometax)*6
        ytdincometax7 = (incometax)*7
        monthlyssf = 0.13*mgross
        ytdssf = monthlyssf*1
        ytdssf2 = monthlyssf*2
        ytdssf3 = monthlyssf*3
        ytdssf4 = monthlyssf*4
        ytdssf5 = monthlyssf*5
        ytdssf6 = monthlyssf*6
        ytdssf7 = monthlyssf*7
        monsal = mgross
        premium = generator.generate_random_numbers(500, 1000, 1)[0]
        bonus = generator.generate_random_numbers(400, 900, 1)[0]
        union1 = int(generator.generate_random_numbers(60, 100, 1)[0])
        union2 = int(generator.generate_random_numbers(60, 100, 1)[0])
        union3 = int(generator.generate_random_numbers(60, 100, 1)[0])
        siclife = int(generator.generate_random_numbers(60, 100, 1)[0])

        tpayments = monsal+premium+bonus
        tdeduct = sscemp+incometax+union1+union2+siclife+union3

        sal = tpayments-tdeduct
        sal = 2750

        postsal = round(vul.random.uniform(20000, 50000), 2)

        bank = bn
        if bn == 'om':
            bank = 'Omnibank'
        elif bn == 'stan':
            bank = 'Stanbic'
        elif bn == 'nib':
            bank = 'NIB LTD'
        elif bn == 'adb':
            bank = 'ADB'
        elif bn == 'gcb':
            bank = 'GCB LTD'
        elif bn == 'fid':
            bank = 'Fidelity Bank'
        
        

        work_date = vul.add_day_and_format(dob, 23)

        clean_firstname = firstname.replace(' ', '').replace('-', '').lower()
        clean_lastname = lastname.replace(' ', '').replace('-', '').lower()
        email2 = clean_firstname+clean_lastname+str(vul.random.randint(1, 100))
        emailme.create_email(email2, email, "linda@workgh.com")
        email2all = email2 + '@workgh.com'

        # Example Usage
        selected_interests = schooldatas.select_random_items('specific_interests')
        selected_skills = schooldatas.select_random_items('specific_skills')
        selected_achievements = schooldatas.select_random_items('achievements')
        selected_activities = schooldatas.select_random_items('extracurricular_activities')

        print("Selected Interests:", selected_interests)
        print("Selected Skills:", selected_skills)
        print("Selected Achievements:", selected_achievements)
        print("Selected Activities:", selected_activities)

        previous_university = schooldatas.get_previous_uni(university)

        if university == 'central':
            proname = 'Ophelia Delali Zungbey (Mrs)'
            prosig = 'Zungbey'
            proemail  = things.get_first_name(proname) + prosig
            proemail = proemail.lower()
        
        else :
            proname = vul.generate_random_name()
            proemail = prosig  = things.get_first_name(proname)
            proemail = proemail.lower()

        bank2 = "EQUITY SAVINGS AND LOANS LTD"
        
        minute = vul.random.randint(0,60)
        hour = vul.random.randint(8,17)

        # Variables common to all templates
        template_vars_common = {
            'lastname': lastname,
            'firstname': firstname,
            'sex': sex,
            'rol': rol,
            'current_year': current_year,
            'named': named,
            'passportn': passportn,
            'myaddress': addresss,
            'phonen': phonen,
            'mycity': mycity,
            'firstname': firstname,
            'lastname': lastname,
            'branch': branch,
            'bn': bn,
            'ssn': ssn,
            'mr': mr,
            'se': se,
            'him': him,
            'his': his,
            'he': he,
            'region': region,
            'nationality': nationality,
            'district': branch,
            'staffid': staffid,
            'postsal': postsal,
            'network': network,
            'sal': sal,
            'signday': vul.add_day_and_format(vul.datetime.now(), 1),
            'acc': acc,
            'min': min,
            'employer': employer,
            'dept': dept,
            'role': role,
            'work': work,
            'unionlab1': unionlab1,
            'unionlab2': unionlab2,
            'unionlab3': unionlab3,
            'typer': typer,
            'cost': cost,
            'retention': retention,
            'work_date': work_date,
            'course': course,
            'university': university,
            'gradyear': gradyear,
            'myclass': myclass,
            'proname': proname,
            'proemail': proemail,
            'prosig': prosig,
            'startyear': int(gradyear) - 4,
            'email2all': email2all,
            'addresss': addresss,
            'current_year': current_year,
            'mymonth': dob.strftime('%B'),
            'myyear': dob.strftime('%Y'),
            'myday': dob.strftime('%d'),
            'fromcountry': fromcountry,
            'destination': destination,
            'lian': lian,
            'tostudy': tostudy,
            'hassal': 1,
            'bank2': bank2
        }

        transactions = []
        summary = []
        chunks = []
        top_date = ''
        stamp_date = ''

        poststudy = sul.getemployed()[0]
        sign_date = vul.add_day_and_format(vul.datetime.now(), 60)

        end_date = vul.datetime.now().strftime("%Y-%m-%d")
        initial_balance = round(vul.random.uniform(50000, 70000), 2)
        
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
            initial_balance = round(vul.random.uniform(220000, 300000), 2)
            transactions, summary = bk2.generate_random_transactions_gcb(template_vars_common, initial_balance, sal)
        elif bn == 'nib':
            start = 10
            continue_from = 10
            initial_balance = round(vul.random.uniform(380000, 410000), 2)
            transactions, summary = bk2.generate_random_transactions_nib_school(template_vars_common, initial_balance, sal)
        
        
        last_transaction_date = vul.objme(summary['last_transaction_date'])
        top_date = vul.formatmydate(last_transaction_date, ("%d %B %Y"))
        stamp_date = vul.formatmydate(last_transaction_date, ("%d/%m/%Y"))

        first_page_transactions = transactions[:start]
        subsequent_page_transactions = transactions[start:]
        chunks = [first_page_transactions] + [subsequent_page_transactions[i:i+continue_from] for i in range(0, len(subsequent_page_transactions), continue_from)]
        
        jobs = sul.get_jobs('education', 3)

        if cv == '':
            vul.render_html_to_pdf('/packaging/cv.html', os.path.join(student_folder, 'cv.html'), document_paths['cv'][1], {**template_vars_common, 'jobs': jobs, 'selected_interest':selected_interests, 'selected_achievements':selected_achievements, 'selected_skills':selected_skills, 'selected_activities':selected_activities, 'prev':previous_university}, options)

        vul.render_html_to_pdf(f'/packaging/{bn}.html', os.path.join(student_folder, 'stan.html'), document_paths['stan'][1] , {**template_vars_common, 'transactions':transactions,'chunks':chunks, 'summary':summary, 'top_date':top_date, 'stamp_date':stamp_date, 'towords':things.convert_amount_to_words(float(summary['closing_balance'].replace(',',''))), 'openedon': vul.add_day_and_format(emp_start,50)}, options)

        # vul.render_html_to_pdf('/packaging/ukstudycover.html', os.path.join(student_folder, 'ukstudycover.html'),document_paths['ukstudycover'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y"), 'poststudy':poststudy, 'last_transaction_date':last_transaction_date, 'sign_date':sign_date}, options)
        
        vul.render_html_to_pdf('/packaging/invoice.html', os.path.join(student_folder, 'invoice.html'), document_paths['invoice'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y"), 'poststudy':poststudy, 'last_transaction_date':last_transaction_date, 'sign_date':sign_date}, options)

        vul.render_html_to_pdf('/packaging/profi.html', os.path.join(student_folder, 'profi.html'), document_paths['profi'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y"), 'poststudy':poststudy, 'last_transaction_date':last_transaction_date, 'sign_date':sign_date, 'prev':previous_university}, options)

        vul.render_html_to_pdf('/packaging/legonref.html', os.path.join(student_folder, 'schoolref.html'), document_paths['legonref'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y"), 'poststudy':poststudy, 'last_transaction_date':last_transaction_date, 'sign_date':sign_date, 'prev':previous_university}, options)

        vul.render_html_to_pdf('/packaging/sponsorme.html', os.path.join(student_folder, 'sponsorme.html'),document_paths['sponsorme'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y"), 'poststudy':poststudy, 'last_transaction_date':last_transaction_date, 'sign_date':sign_date}, options)
        
        vul.render_html_to_pdf('/packaging/credit.html', os.path.join(student_folder, 'credit.html'),document_paths['credit'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y"), 'hour':hour, 'minute':minute}, options)

        vul.render_html_to_pdf('/packaging/poststudy.html', os.path.join(student_folder, 'poststudy.html'),document_paths['poststudy'][1], {**template_vars_common, 'dateprinted':stamp_date, 'dob':dob.strftime("%d/%m/%Y"), 'poststudy':poststudy, 'last_transaction_date':last_transaction_date, 'sign_date':sign_date}, options)

        vul.render_html_to_pdf('/packaging/mar.html', os.path.join(student_folder, 'mar.html'),document_paths['mar'][1], {**template_vars_common, 'branch':branch, 'bank': bank, 'ytdssf':"{:,.2f}".format(ytdssf3), 'monthlyssf':"{:,.2f}".format(monthlyssf), 'ytdincometax':"{:,.2f}".format(ytdincometax3), 
                                                                                                    'mgross':"{:,.2f}".format(mgross), 'ytdgrosspay':"{:,.2f}".format(ytdgrosspay3), 'anualsal': "{:,.2f}".format(anualsal),'union3':"{:,.2f}".format(union3), 'siclife':"{:,.2f}".format(siclife), 'union2': "{:,.2f}".format(union2),
                                                                                                    'union1':"{:,.2f}".format(union1), 'incometax': "{:,.2f}".format(incometax),'sscemp':"{:,.2f}".format(sscemp), 'cost':cost, 'bonus': "{:,.2f}".format(bonus), 'premium': "{:,.2f}".format(premium), 'monsal':"{:,.2f}".format(monsal), 'tpayments': "{:,.2f}".format(tpayments),'tdeduct':"{:,.2f}".format(tdeduct),'ytdssfworker': "{:,.2f}".format(ytdssfworker3), 'salary':"{:,.2f}".format(sal)}, options)
                
        vul.render_html_to_pdf('/packaging/apr.html', os.path.join(student_folder, 'apr.html'),document_paths['apr'][1], {**template_vars_common, 'branch':branch, 'bank': bank, 'ytdssf':"{:,.2f}".format(ytdssf4), 'monthlyssf':"{:,.2f}".format(monthlyssf), 'ytdincometax':"{:,.2f}".format(ytdincometax4), 
                                                                                                'mgross':"{:,.2f}".format(mgross), 'ytdgrosspay':"{:,.2f}".format(ytdgrosspay4), 'anualsal': "{:,.2f}".format(anualsal),'union3':"{:,.2f}".format(union3), 'siclife':"{:,.2f}".format(siclife), 'union2': "{:,.2f}".format(union2),
                                                                                                'union1':"{:,.2f}".format(union1), 'incometax': "{:,.2f}".format(incometax),'sscemp':"{:,.2f}".format(sscemp), 'cost':cost, 'bonus': "{:,.2f}".format(bonus), 'premium': "{:,.2f}".format(premium), 'monsal':"{:,.2f}".format(monsal), 'tpayments': "{:,.2f}".format(tpayments),'tdeduct':"{:,.2f}".format(tdeduct),'ytdssfworker': "{:,.2f}".format(ytdssfworker4), 'salary':"{:,.2f}".format(sal)}, options)

        vul.render_html_to_pdf('/packaging/may.html', os.path.join(student_folder, 'may.html'), document_paths['may'][1], {**template_vars_common, 'branch':branch, 'bank': bank, 'ytdssf':"{:,.2f}".format(ytdssf5), 'monthlyssf':"{:,.2f}".format(monthlyssf), 'ytdincometax':"{:,.2f}".format(ytdincometax5), 
                                                                                                'mgross':"{:,.2f}".format(mgross), 'ytdgrosspay':"{:,.2f}".format(ytdgrosspay5), 'anualsal': "{:,.2f}".format(anualsal),'union3':"{:,.2f}".format(union3), 'siclife':"{:,.2f}".format(siclife), 'union2': "{:,.2f}".format(union2),
                                                                                                'union1':"{:,.2f}".format(union1), 'incometax': "{:,.2f}".format(incometax),'sscemp':"{:,.2f}".format(sscemp), 'cost':cost, 'bonus': "{:,.2f}".format(bonus), 'premium': "{:,.2f}".format(premium), 'monsal':"{:,.2f}".format(monsal), 'tpayments': "{:,.2f}".format(tpayments),'tdeduct':"{:,.2f}".format(tdeduct),'ytdssfworker': "{:,.2f}".format(ytdssfworker5), 'salary':"{:,.2f}".format(sal)}, options)

        vul.render_html_to_pdf('/packaging/jun.html', os.path.join(student_folder, 'jun.html'), document_paths['jun'][1], {**template_vars_common, 'branch':branch, 'bank': bank, 'ytdssf':"{:,.2f}".format(ytdssf6), 'monthlyssf':"{:,.2f}".format(monthlyssf), 'ytdincometax':"{:,.2f}".format(ytdincometax6), 
                                                                                                'mgross':"{:,.2f}".format(mgross), 'ytdgrosspay':"{:,.2f}".format(ytdgrosspay6), 'anualsal': "{:,.2f}".format(anualsal),'union3':"{:,.2f}".format(union3), 'siclife':"{:,.2f}".format(siclife), 'union2': "{:,.2f}".format(union2),
                                                                                                'union1':"{:,.2f}".format(union1), 'incometax': "{:,.2f}".format(incometax),'sscemp':"{:,.2f}".format(sscemp), 'cost':cost, 'bonus': "{:,.2f}".format(bonus), 'premium': "{:,.2f}".format(premium), 'monsal':"{:,.2f}".format(monsal), 'tpayments': "{:,.2f}".format(tpayments),'tdeduct':"{:,.2f}".format(tdeduct),'ytdssfworker': "{:,.2f}".format(ytdssfworker6), 'salary':"{:,.2f}".format(sal)}, options)

        vul.render_html_to_pdf('/packaging/jul.html', os.path.join(student_folder, 'jul.html'), document_paths['jul'][1], {**template_vars_common, 'branch':branch, 'bank': bank, 'ytdssf':"{:,.2f}".format(ytdssf7), 'monthlyssf':"{:,.2f}".format(monthlyssf), 'ytdincometax':"{:,.2f}".format(ytdincometax6), 
                                                                                                'mgross':"{:,.2f}".format(mgross), 'ytdgrosspay':"{:,.2f}".format(ytdgrosspay7), 'anualsal': "{:,.2f}".format(anualsal),'union3':"{:,.2f}".format(union3), 'siclife':"{:,.2f}".format(siclife), 'union2': "{:,.2f}".format(union2),
                                                                                                'union1':"{:,.2f}".format(union1), 'incometax': "{:,.2f}".format(incometax),'sscemp':"{:,.2f}".format(sscemp), 'cost':cost, 'bonus': "{:,.2f}".format(bonus), 'premium': "{:,.2f}".format(premium), 'monsal':"{:,.2f}".format(monsal), 'tpayments': "{:,.2f}".format(tpayments),'tdeduct':"{:,.2f}".format(tdeduct),'ytdssfworker': "{:,.2f}".format(ytdssfworker7), 'salary':"{:,.2f}".format(sal)}, options)

        
        time.sleep(20)
        my_cv = os.path.join(student_folder, 'cv.pdf')

        # Example Usage
        category_input = tostudy  # Change this to the desired category
        
            
        pdf_files = ['may.pdf','jun.pdf','jul.pdf']

        output_pdf = 'payslip.pdf'

        # # # Merge PDFs
        vul.merge_pdfs(student_folder, pdf_files, output_pdf)

        clean_firstname = firstname.replace(' ', '').replace('-', '').lower()
        clean_lastname = lastname.replace(' ', '').replace('-', '').lower()
        # emailme.create_email(clean_firstname + clean_lastname, email)

        vul.compress_pdf(os.path.join(student_folder, 'passport.pdf'), os.path.join(student_folder, 'mypassport.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'cv.pdf'), os.path.join(student_folder, 'mycv.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'degree.pdf'), os.path.join(student_folder, 'mydegree.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'transcript.pdf'), os.path.join(student_folder, 'mytranscript.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'wassce.pdf'), os.path.join(student_folder, 'mywassce.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'credit.pdf'), os.path.join(student_folder, 'mycredit.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'poststudy.pdf'), os.path.join(student_folder, 'mypoststudy.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'payslip.pdf'), os.path.join(student_folder, 'mypayslip.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'invoice.pdf'), os.path.join(student_folder, 'myinvoice.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'stan.pdf'), os.path.join(student_folder, 'mystatement.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'legonref.pdf'), os.path.join(student_folder, 'myschoolref.pdf'))

        attachment_paths_to_student = [
            os.path.join(student_folder, 'myinvoice.pdf'),
        ]

        vul.send_email(
            recipient_email=email,
            subject=f"{firstname} {lastname} - Welcome To WAAP Travels",
            body=f"Your address: {addresss}, Please kindly find attached your invoice.",
            attachment_paths=attachment_paths_to_student
        )
        
        courses_in_category = schooldatas.select_courses_by_category(category_input, "kc")

        max_iterations = 3

        #Loop through courses_in_category, limiting to a maximum of 7 iterations
        for soploop in range(max_iterations):
            sopname = 'sop' + str(soploop + 1)  # soploop starts from 0, so add 1 for naming
            course_now = courses_in_category[soploop]['course']
            university_now = courses_in_category[soploop]['university']

            template_vars_common[f'university{soploop + 1}'] = university_now
            template_vars_common[f'course{soploop + 1}'] = course_now
            
            # Generate the SOP using the provided function
            sop = cvsop.dosop(my_cv, course_now, university_now)
            
            # Render the SOP to HTML and save as PDF
            vul.render_html_to_pdf(
                '/packaging/sop.html', 
                os.path.join(student_folder, f'{university_now}_sop.html'), 
                document_paths[sopname][1], 
                {**template_vars_common, 'sop': sop}, 
                options
            )
        
        vul.compress_pdf(os.path.join(student_folder, 'sop1.pdf'), os.path.join(student_folder, 'sop_1.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop2.pdf'), os.path.join(student_folder, 'sop_2.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop3.pdf'), os.path.join(student_folder, 'sop_3.pdf'))
        
        attachment_paths_kc = [
            os.path.join(student_folder, 'mycv.pdf'),
            os.path.join(student_folder, 'myschoolref.pdf'),
            os.path.join(student_folder, 'mydegree.pdf'),
            os.path.join(student_folder, 'mytranscript.pdf'),
            os.path.join(student_folder, 'mywassce.pdf'),
            os.path.join(student_folder, 'mypassport.pdf'),
            os.path.join(student_folder, 'sop_1.pdf'),
            os.path.join(student_folder, 'sop_2.pdf'),
            os.path.join(student_folder, 'sop_3.pdf'),
        ]
        
        vul.send_email(
            recipient_email="ella@workgh.com",
            subject=f"{firstname} {lastname} - New Application KC-Overseas",
            body=f"Email to use: {email2all} address: {addresss}",
            attachment_paths=attachment_paths_kc
        )
        
        courses_in_category = schooldatas.select_courses_by_category(category_input, "ed")

    # Determine the maximum number of iterations (up to 7)
        max_iterations = 3

        #Loop through courses_in_category, limiting to a maximum of 7 iterations
        for soploop in range(max_iterations):
            sopname = 'sop_' + str(soploop + 1)  # soploop starts from 0, so add 1 for naming
            course_now = courses_in_category[soploop]['course']
            university_now = courses_in_category[soploop]['university']

            template_vars_common[f'university{soploop + 1}'] = university_now
            template_vars_common[f'course{soploop + 1}'] = course_now
            
            # Generate the SOP using the provided function
            sop = cvsop.dosop(my_cv, course_now, university_now)
            
            # Render the SOP to HTML and save as PDF
            vul.render_html_to_pdf(
                '/packaging/sop.html', 
                os.path.join(student_folder, f'{university_now}_sop.html'), 
                document_paths[sopname][1], 
                {**template_vars_common, 'sop': sop}, 
                options
            )
        
        vul.compress_pdf(os.path.join(student_folder, 'sop_1.pdf'), os.path.join(student_folder, 'sop__1.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop_2.pdf'), os.path.join(student_folder, 'sop__2.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop_3.pdf'), os.path.join(student_folder, 'sop__3.pdf'))
        
        attachment_paths_edvoy = [
            os.path.join(student_folder, 'mycv.pdf'),
            os.path.join(student_folder, 'myschoolref.pdf'),
            os.path.join(student_folder, 'mydegree.pdf'),
            os.path.join(student_folder, 'mytranscript.pdf'),
            os.path.join(student_folder, 'mywassce.pdf'),
            os.path.join(student_folder, 'mypassport.pdf'),
            os.path.join(student_folder, 'sop__1.pdf'),
            os.path.join(student_folder, 'sop__1.pdf'),
            os.path.join(student_folder, 'sop__1.pdf'),
        ]
        
        vul.send_email(
            recipient_email="ella@workgh.com",
            subject=f"{firstname} {lastname} - New Application Edvoy",
            body=f"Email to use: {email2all} address: {addresss}",
            attachment_paths=attachment_paths_edvoy
        )
        
        
        courses_in_category = schooldatas.select_courses_by_category(category_input, "ab")

    # Determine the maximum number of iterations (up to 7)
        max_iterations = 5

        #Loop through courses_in_category, limiting to a maximum of 7 iterations
        for soploop in range(max_iterations):
            sopname = 'sop__' + str(soploop + 1)  # soploop starts from 0, so add 1 for naming
            course_now = courses_in_category[soploop]['course']
            university_now = courses_in_category[soploop]['university']

            template_vars_common[f'university{soploop + 1}'] = university_now
            template_vars_common[f'course{soploop + 1}'] = course_now
            
            # Generate the SOP using the provided function
            sop = cvsop.dosop(my_cv, course_now, university_now)
            
            # Render the SOP to HTML and save as PDF
            vul.render_html_to_pdf(
                '/packaging/sop.html', 
                os.path.join(student_folder, f'{university_now}_sop.html'), 
                document_paths[sopname][1], 
                {**template_vars_common, 'sop': sop}, 
                options
            )
        
        vul.compress_pdf(os.path.join(student_folder, 'sop__1.pdf'), os.path.join(student_folder, 'sop___1.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop__2.pdf'), os.path.join(student_folder, 'sop___2.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop__3.pdf'), os.path.join(student_folder, 'sop___3.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop__4.pdf'), os.path.join(student_folder, 'sop___4.pdf'))
        vul.compress_pdf(os.path.join(student_folder, 'sop__5.pdf'), os.path.join(student_folder, 'sop___5.pdf'))
        
        
        attachment_paths_applyboard = [
            os.path.join(student_folder, 'mycv.pdf'),
            os.path.join(student_folder, 'myschoolref.pdf'),
            os.path.join(student_folder, 'mydegree.pdf'),
            os.path.join(student_folder, 'mytranscript.pdf'),
            os.path.join(student_folder, 'mywassce.pdf'),
            os.path.join(student_folder, 'mypassport.pdf'),
            os.path.join(student_folder, 'sop___1.pdf'),
            os.path.join(student_folder, 'sop___2.pdf'),
            os.path.join(student_folder, 'sop___3.pdf'),
            os.path.join(student_folder, 'sop___4.pdf'),
            os.path.join(student_folder, 'sop___5.pdf'),
        ]
        
        vul.send_email(
            recipient_email="joseph@workgh.com",
            subject=f"{firstname} {lastname} - New Application on Applyboard",
            body=f"Email to use: {email2all} address: {addresss}",
            attachment_paths=attachment_paths_applyboard
        )

        
        
        attachment_paths = [
            os.path.join(student_folder, 'mypassport.pdf'),
            os.path.join(student_folder, 'mycredit.pdf'),
            os.path.join(student_folder, 'mypoststudy.pdf'),
            os.path.join(student_folder, 'mypayslip.pdf'),
            os.path.join(student_folder, 'mystatement.pdf'),
        ]
        
        vul.send_email(
            recipient_email="linda@workgh.com",
            subject=f"{firstname} {lastname} - Prodigy Finance",
            body=f"Email to use: {email2all} address: {addresss}",
            attachment_paths=attachment_paths
        )

        return "good"


    response = requests.get(API_URL)
        
    if response.status_code == 200:
        all_students = response.json()
        print("Fetched all student details.")

        # Filter students where status is 'new'
        new_students = [student for student in all_students if student['student_status'] == 'new']
        
        if new_students:
            print(f"Found {len(new_students)} student(s) with status 'new'.")
            # Process each student with 'new' status
            for student in new_students:
                do_student(student)
                update_student_status(student['id'], 'ready')
        else:
            print("No students with status 'new' found.")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")


    return "good"
