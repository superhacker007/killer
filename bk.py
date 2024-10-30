from flask import render_template_string
from datetime import datetime, timedelta
import random
import string
import calendar, os, vul

def generate_random_reference():
    return 'FT222' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def generate_detailed_description_nib(is_debit, amount, firstname, lastname, branch, staffid, phonen, mycity, network):
    descriptions = []  # Initialize descriptions
    if is_debit:
        if amount < 50:
            descriptions = [
                {"short": "Bank Charges", "long": "Bank charges for transaction"},
                {"short": "Airtime", "long": f"Airtime Purchase {network} Momo"}
            ]
        elif 50 <= amount < 200:
            descriptions = [
                {"short": "Utility", "long": "ECG Prepaid Topup"},
                {"short": "Airtime Top-up", "long": f"Airtime Purchase {network} Momo"}
            ]
        elif 200 <= amount < 1000:
            descriptions = [
                {"short": "Transfer", "long": f"Transfer to {random.choice(vul.first_names).upper() + ' ' + lastname}"},
                {"short": "POS Debit", "long": f"Grocery shopping at {mycity} mall"},
                {"short": "ATM Withdrawal", "long": f"Cash withdrawal from {branch} ATM"}
            ]
        else:
            descriptions = [
                {"short": "Transfer", "long": f"Transfer to {random.choice(vul.first_names).upper()+ ' ' +lastname}"},
                {"short": "Bank To Wallet", "long": f"MoMo Transfer to {phonen}"},
                {"short": "Transfer", "long": f"funds transfer"}
            ]
    else:
        if amount < 50:
            descriptions = [
                {"short": "Interest", "long": "Interest on savings account"},
                {"short": "Refund", "long": "Small refund for transaction"}
            ]
        elif 50 <= amount < 200:
            descriptions = [
                {"short": "Bonus", "long": "Bonus for project completion"},
                {"short": "Refund", "long": f"Refund for order {staffid}"}
            ]
        else:
            descriptions = [
                {"short": "Cash Deposit", "long": f"Cash Deposit by {random.choice(vul.first_names).upper() + ' ' + lastname}"},
                {"short": "Check Deposit", "long": f"Check Deposit by {random.choice(vul.first_names).upper() + ' ' + lastname}"},
                {"short": "Wallet to Bank", "long": f"MoMo wallet to bank transfer from {phonen}"},
            ]
    return random.choice(descriptions)

def generate_detailed_description(is_debit, acc, amount, firstname, lastname, branch, staffid, phonen, mycity, network):
    descriptions = []  # Initialize descriptions
    if is_debit:
        if amount < 50:
            descriptions = [
                {"short": "Bank Charges", "long": f"{branch} BRANCH, E-BANKING CHARGE; E-Banking Charges"},
                {"short": "Airtime", "long": f"Airtime Purchase {network} Momo"}
            ]
        elif 50 <= amount < 200:
            descriptions = [
                {"short": "Utility", "long": f"ECG Prepaid Topup {branch} BRANCH, E-WALLET TRANS; "},
                {"short": "Airtime Top-up", "long": f"Airtime Purchase {network} Momo {branch} BRANCH: ACCOUNT TO WALLET; FBGMA NSANO; {lastname}"}
            ]
        elif 200 <= amount < 1000:
            descriptions = [
                {"short": "Transfer", "long": f"{branch} BRANCH: ACCOUNT TO WALLET; FBGMA NSANO CREDIT FROM AC {acc} TO {network} {phonen}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: ACCOUNT TO WALLET; FBGMA NSANO CREDIT FROM AC {acc} TO {network} {phonen}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: ACCOUNT TO WALLET; FBGMA NSANO CREDIT FROM AC {acc} TO {network} {phonen}; {lastname}"}
            ]
        else:
            descriptions = [
                {"short": "Transfer", "long": f"{branch} BRANCH: ACCOUNT TO WALLET; FBGMA NSANO CREDIT FROM AC {acc} TO {network} {phonen}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: CASH WITHDRAWAL; CHEQ BY {firstname} {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: ACCOUNT TO WALLET; FBGMA NSANO CREDIT FROM AC {acc} TO {network} {phonen}; {lastname}"}
            ]
    else:
        if amount < 50:
            descriptions = [
                {"short": "Interest", "long": "Interest on savings account"},
                {"short": "Refund", "long": "Small refund for transaction"}
            ]
        elif 50 <= amount < 200:
            descriptions = [
                {"short": "Refund", "long": f"{branch} BRANCH: Refund for order {staffid}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
            ]
        else:
            descriptions = [
                {"short": "Transfer", "long": f"{branch} BRANCH: CHEQUE DEPOSIT; CHEQ BY {random.choice(vul.first_male_names).upper()} {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"}
            ]
    return random.choice(descriptions)

def get_last_business_day(year, month):
    last_day = calendar.monthrange(year, month)[1]
    last_date = datetime(year, month, last_day)
    while last_date.weekday() >= 5:  # Saturday or Sunday
        last_date -= timedelta(days=1)
    return last_date

def generate_transactions(sal, acc, firstname, lastname, branch, staffid, phonen, mycity, network):
    num_months = 5
    today = datetime.today()
    start_date = (today - timedelta(days=30 * num_months)).replace(day=1)
    end_date = today if today.weekday() < 5 else today - timedelta(days=today.weekday() - 4)
    opening_balance_original = round(random.uniform(100000, 200000), 2)
    current_balance = opening_balance_original - sal
    opening_balance = opening_balance_original
    transactions = []

    total_debits = 0.0
    total_credits = 0.0

    # Generate transactions for each month in the past 5 months
    for month_offset in range(num_months):
        current_month = (start_date.month + month_offset - 1) % 12 + 1
        current_year = start_date.year + (start_date.month + month_offset - 1) // 12

        last_business_day = get_last_business_day(current_year, current_month)
        num_transactions = random.randint(8, 14)

        # Ensure salary is paid on the last business day of each month
        salary_description = f"HEAD OFFICE SALARY PROCESSING; {calendar.month_name[current_month][:3].upper()} {str(current_year)[-2:]} SAL PAYMNT B/O CAG"
        transactions.append({
            'date': last_business_day.strftime('%d %b %Y'),
            'reference': generate_random_reference(),
            'description': "Salary",
            'valueDate': last_business_day.strftime('%d %b %Y'),
            'debit': '',
            'credit': "{:,.2f}".format(sal),
            'closingBalance': "{:,.2f}".format(current_balance + sal),
            'detailedDescription': salary_description
        })
        current_balance += sal
        total_credits += sal

        # Generate random transactions for the current month
        transaction_dates = [
            datetime(current_year, current_month, 1) + timedelta(days=x)
            for x in range((last_business_day - datetime(current_year, current_month, 1)).days + 1)
            if (datetime(current_year, current_month, 1) + timedelta(days=x)).weekday() < 5
        ]

        # Adjust the number of transactions to be sampled if necessary
        num_transactions = min(num_transactions - 1, len(transaction_dates))

        transaction_dates = sorted(random.sample(transaction_dates, num_transactions))

        for date in transaction_dates:
            if date == last_business_day:
                continue

            if random.choice([True, False]):
                amount = random.randint(1, 100) * 10  # Debit amounts < 2000
                debit = amount
                credit = ''
                current_balance -= debit
                total_debits += debit
                description = generate_detailed_description(True, acc, amount, firstname, lastname, branch, staffid, phonen, mycity, network)
                short_description = description["short"]
                long_description = description["long"]
            else:
                amount = random.randint(10, 500) * 10  # Credit amounts
                debit = ''
                credit = amount
                current_balance += credit
                total_credits += credit
                description = generate_detailed_description(False, acc, amount, firstname, lastname, branch, staffid, phonen, mycity, network)
                short_description = description["short"]
                long_description = description["long"]

            transactions.append({
                'date': date.strftime('%d %b %Y'),
                'reference': generate_random_reference(),
                'description': short_description,
                'valueDate': date.strftime('%d %b %Y'),
                'debit': "{:,.2f}".format(debit) if debit != '' else '',
                'credit': "{:,.2f}".format(credit) if credit != '' else '',
                'closingBalance': "{:,.2f}".format(current_balance),
                'detailedDescription': long_description
            })

    # Handle transactions for the current month
    current_month = today.month
    current_year = today.year
    last_business_day = get_last_business_day(current_year, current_month)
    num_transactions = random.randint(7, 12) if today.day > 20 else random.randint(2, 5)

    # Ensure salary is paid on the last business day of the current month if today is at least the last business day
    if today >= last_business_day:
        salary_description = f"{calendar.month_name[current_month][:3].upper()} {str(current_year)[-2:]} salary payment"
        transactions.append({
            'date': last_business_day.strftime('%d %b %Y'),
            'reference': generate_random_reference(),
            'description': "Salary",
            'valueDate': last_business_day.strftime('%d %b %Y'),
            'debit': '',
            'credit': "{:,.2f}".format(sal),
            'closingBalance': "{:,.2f}".format(current_balance + sal),
            'detailedDescription': salary_description
        })
        current_balance += sal
        total_credits += sal

    # Generate random transactions for the current month
    transaction_dates = [
        datetime(current_year, current_month, 1) + timedelta(days=x)
        for x in range((last_business_day - datetime(current_year, current_month, 1)).days + 1)
        if (datetime(current_year, current_month, 1) + timedelta(days=x)).weekday() < 5 and (datetime(current_year, current_month, 1) + timedelta(days=x)) <= end_date
    ]

    # Adjust the number of transactions to be sampled if necessary
    num_transactions = min(num_transactions - 1, len(transaction_dates))

    transaction_dates = sorted(random.sample(transaction_dates, num_transactions))

    # Ensure no date has more than 2 transactions and space out transactions
    date_counts = {}
    for date in transaction_dates:
        date_str = date.strftime('%d %b %Y')
        date_counts[date_str] = date_counts.get(date_str, 0) + 1
        if date_counts[date_str] > 2:
            continue

        if random.choice([True, False]):
            amount = random.randint(1, 200) * 10  # Debit amounts < 2000
            debit = amount
            credit = ''
            current_balance -= debit
            total_debits += debit
            description = generate_detailed_description(True, acc, amount, firstname, lastname, branch, staffid, phonen, mycity, network)
            short_description = description["short"]
            long_description = description["long"]
        else:
            amount = random.randint(10, 500) * 10  # Credit amounts
            debit = ''
            credit = amount
            current_balance += credit
            total_credits += credit
            description = generate_detailed_description(False, acc, amount, firstname, lastname, branch, staffid, phonen, mycity, network)
            short_description = description["short"]
            long_description = description["long"]

        transactions.append({
            'date': date_str,
            'reference': generate_random_reference(),
            'description': short_description,
            'valueDate': date_str,
            'debit': "{:,.2f}".format(debit) if debit != '' else '',
            'credit': "{:,.2f}".format(credit) if credit != '' else '',
            'closingBalance': "{:,.2f}".format(current_balance),
            'detailedDescription': long_description
        })

    transactions.sort(key=lambda x: datetime.strptime(x['date'], '%d %b %Y'))
    first_transaction_date = transactions[0]['date'] if transactions else None

    return transactions, "{:,.2f}".format(opening_balance), "{:,.2f}".format(current_balance), first_transaction_date, opening_balance_original, "{:,.2f}".format(total_debits), "{:,.2f}".format(total_credits)

html_template_fide = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fidelity Bank Statement</title>
    <script>
        function formatCurrency(amount) {
            return new Intl.NumberFormat('en-US', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).format(amount);
        }

        document.addEventListener('DOMContentLoaded', (event) => {
            const amountElement = document.getElementById('amount');
            let amount = amountElement.textContent;
            // Remove commas from the string
            amount = amount.replace(/,/g, '');
            // Convert the cleaned string to a float
            amount = parseFloat(amount);
            amountElement.textContent = formatCurrency(amount);
        });
    </script>
    <style>
        body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    font-size: 13px;
}

.container {
    width: 210mm;
    padding: 0 7mm;
    background-color: #fff;
    background-repeat: no-repeat;
    background-size: 760px 100px;
    background-position: 20px 600px;
    box-sizing: border-box;
    background-image: url('https://veesupportservices.co.uk/b/bgfide.png');
}

.header img {
    width: 180mm;
    height: 90px;
    margin: 0 auto;
}

.statement-header {
    text-align: left;
    margin-bottom: 20px;
}

.statement-header img {
    width: 270px;
    margin-left: 15px;
    margin-bottom: -25px;
}

.account-details {
    display: flex;
    justify-content: space-between;
}

.account-holder {
    border: 1px solid #e1dcdc;
    padding: 10px 50px;
    width: 33%;
    margin-top: 40px;
    border-radius: 20px;
} 

.account-info {
    width: 60%;
    margin-left: 110px;
}

.account-holder p {
    margin: 0;
    padding: 2px 0;
    line-height: 2em;
}

.account-info td {
    border: 1px solid #e1dcdc;
    padding: 5px;
    font-size: 14px;
}

.account-info td:nth-child(odd) {
    color: darkgrey;
}

.account-info tr {
    border: 1px solid #e1dcdc;
    padding: 5px;
    border-collapse: separate;
    height: 35px;
}

.maintab {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.maintab, th, td {
    border: 2px solid black;
    padding: 5px 2px;
}

.maintab td, .maintab th {
    vertical-align: middle; text-align: center;
}

.maintab td:nth-child(2) {
    text-align: left;
    padding: 7px 2px 2px 3px;
    line-height: 1.27em;
}

th {
    background-color: #8f8d8d;
}

td {
    vertical-align: top;
}

    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://veesupportservices.co.uk/b/topfide.png" alt="">
        </div>
        <div class="statement-header">
            <img src="https://veesupportservices.co.uk/b/statefide.png" alt="">
            <div class="account-details">
                <div class="account-holder">
                    <p>{{firstname}} {{lastname}}</p>
                    <p>{{branch}}</p>
                    <p>{{addresss}}, {{mycity}}</p>
                </div>
                <div class="account-info">
                    <table>
                        <tr>
                            <td>Branch:</td>
                            <td>{{branch}}</td>
                        </tr>
                        <tr>
                            <td>Currency:</td>
                            <td>GHS</td>
                        </tr>
                        <tr>
                            <td>Account Number:</td>
                            <td>{{acc}}</td>
                        </tr>
                        <tr>
                            <td>Statement Date:</td>
                            <td>{{ first_transaction_date }} To {{date_printed}}</td>
                        </tr>
                        <tr>
                            <td>Opening Balance:</td>
                            <td id="amount">{{ start_balance - sal }}</td>
                        </tr>
                        <tr>
                            <td>Closing Balance:</td>
                            <td>{{ closing_balance }}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <img src="https://veesupportservices.co.uk/b/signfide.png" style="position: absolute; margin: -150px 180px;" alt="">
        </div>
        <table class="maintab">
            <thead>
                <tr style="height: 45px;">
                    <th style="width: 80px;">DATE</th>
                    <th>DESCRIPTION</th>
                    <th style="width: 85px;">VALUE DATE</th>
                    <th style="width: 80px;">DEBIT</th>
                    <th style="width: 80px;">CREDIT</th>
                    <th style="width: 80px;">BALANCE</th>
                </tr>
            </thead>
            <tbody>
                
                {% for transaction in transactions %}
                <tr>
                    <td>{{ transaction.date }}</td>
                    <td>{{ transaction.detailedDescription }}</td>
                    <td>{{ transaction.date }}</td>
                    <td>{{ transaction.debit }}</td>
                    <td>{{ transaction.credit }}</td>
                    <td>{{ transaction.closingBalance }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <table>
            <tbody>
                <tr style="border:none;">
                    <td style="border:none; width: 80px;" >Turnover:</td>
                    <td style="border:none; width: 330px;"></td>
                    <td style="border:none; width: 85px;"></td>
                    <td style="border:none; width: 80px;">{{ total_debits }}</td>
                    <td style="border:none; width: 80px;">{{ total_credits }}</td>
                    <td style="border:none; width: 80px;"></td>
                </tr>
            </tbody>
        </table>
        <img src="https://veesupportservices.co.uk/b/signfide.png" style="position: absolute; margin: 100px 180px; width: 150px" alt="">
        <p><img src="https://veesupportservices.co.uk/b/checkfor.png" alt="" style="width: 700px; align-content: center;"></p>
    </div>
</body>
</html>

'''

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Currency Formatting</title>
    <script>
        function formatCurrency(amount) {
            return new Intl.NumberFormat('en-US', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }).format(amount);
        }

        document.addEventListener('DOMContentLoaded', (event) => {
            const amountElement = document.getElementById('amount');
            let amount = amountElement.textContent;
            // Remove commas from the string
            amount = amount.replace(/,/g, '');
            // Convert the cleaned string to a float
            amount = parseFloat(amount);
            amountElement.textContent = formatCurrency(amount);
        });
    </script>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bank Statement</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            font-size: 8pt;
        }

        .content {
            width: 100%;
            max-width: 210mm; 
            margin: 0 auto;
        }

        .nibtop {
            display: flex;
            background-repeat: no-repeat;
            margin-bottom: 20px;
        }

        .div1 {
            width: 17%;
            padding-top:5%;
            padding-left: 3%;
        }

        .div1 img {
            width: 130px;
        }

        .div2 {
            width: 48%;
            padding: 5%;
            text-align: center;
        }

        .div2 img {
            margin: 0 auto;
            width: 66px;
            height: 67px;
        }


        .div3 {
            width: 26%;
            font-weight: bold;
            padding: 5% 1%;
            font-size: 8pt;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            margin-top: 2%;
        }

        .div4 {
            width: 12%;
            padding: 1%;
            margin: 6%;
            margin-left: -5%;
        }

        table {
            font-family: 'Times New Roman', Times, serif;
            border-collapse: collapse;
            width: 87%;
            margin: 0 auto;
        }

        

        th, td {
            padding: 0;
            text-align: left;
        }

        th {
            background-color: #E8E8E8;
            color: black;
        }

        tr {
            height: 25px; /* Set the desired height for each row */
        }

        tbody tr:nth-child(odd) {
            height: 30pt;
        }

        tbody tr:nth-child(even) {
            background-color: #E8E8E8;
        }

        .background {
            z-index: -100;
            position: absolute;
            margin: 45% 18%;
            opacity: 0.1;
        }

        .background img {
            width: 400px;
        }

        .footer {
            width: 87%;
            margin: 0 auto;
            font-weight: bold;
            font-size: 7.5pt;
        }
        .date {
            margin-left: 600px;
            margin-top: 110px;
            position: absolute;
            font-weight: bold;
            font-size: 10px;
            font-family: 'Times New Roman', Times, serif;
        }
        .owner {
            width: 350px;
            position: absolute;
            margin: 185px 450px;
            font-size: 16px;
            font-family: 'Times New Roman', Times, serif;
        }
        .details {
            position: absolute;
            margin: 125px 50px;
            font-family: 'Times New Roman', Times, serif;
            font-weight: bold;
        }
        .details p {
            line-height: 1.5em;
        }
    </style>
</head>
{% for page in transactions|batch(12, '') %}
<body>
    <div class="content">
        <div class="background">
            <img src="https://veesupportservices.co.uk/b/niblogobg.png" alt="">
        </div>
    <div class="nibtop">
        <div class="div1">
            <img src="https://veesupportservices.co.uk/b/niblogo.png" alt="" width="80%">
        </div>
        <div class="div2">
            <h1>STATEMENT OF ACCOUNT</h1>
            <img src="https://veesupportservices.co.uk/b/nibseal.png" alt="">
        </div>
        <div class="div3">
            <p>
                National Investment Bank Ltd. <br>
                37 Kwame Nkrumah Avenue <br>
                Tel:+233 302 661701 - 10 <br>
                Tel:+233 302 673124 <br>
                www.nibghana.net <br>
                info@nibghana.com <br>
            </p>
        </div>
        <div class="details">
            <p>
                Account Statement <br>
                Branch: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{branch}} <br>
                Account: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{acc}} <br>
                Customer: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{staffid}} <br>
                Currency: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GHS <br>
            </p>
        </div>
        <div class="date">
            {{date_printed}} <br>
            <span style="float: right;">12:48:19</span>
        </div>
        <div class="div4">
            <img src="https://veesupportservices.co.uk/b/logos.png" alt="" width="100%">
        </div>
        <h2 class="owner">{{firstname}} {{lastname}}</h2>
    </div>
        
            <table class="content-table">
                <thead>
                    <tr>
                        <th>Book Date</th>
                        <th>Reference</th>
                        <th>Description</th>
                        <th>Value Date</th>
                        <th>Debit</th>
                        <th>Credit</th>
                        <th>Closing Balance</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background-color: #FFF; height: 14.7pt;">
                        <td>{% if loop.first %} {{first_transaction_date}} {% endif %}</td>
                        <td>{% if loop.first %} Balance at Period Start {% endif %}</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td id="amount">{% if loop.first %} {{start_balance}} {% endif %}</td>
                    </tr>
                    {% for transaction in page %}
                    <tr>
                        <td>{{ transaction.date }}</td>
                        <td>{{ transaction.reference }}</td>
                        <td>{{ transaction.description }}</td>
                        <td>{{ transaction.valueDate }}</td>
                        <td>{{ transaction.debit }}</td>
                        <td>{{ transaction.credit }}</td>
                        <td>{{ transaction.closingBalance }}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td>{{ transaction.detailedDescription }}</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    {% if loop.last %}
                    
                    <tr style="background-color: #FFF;">
                        <td></td>
                        <td></td>
                        <td>Balance at Period <br> End</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td>{{ transaction.closingBalance }}</td>
                    </tr>
                    {% endif %}
                    
                    {% endfor %}
                    
                </tbody>
            </table>

            <div class="footer">
                <img src="https://veesupportservices.co.uk/b/nibstamp.png" alt="" style="position:absolute; width:150px; margin-left: 350px; margin-top: -50px;">
                <p>Please examine this statement carefully. Any error, discrepancy or change of address should be communicated to the Head, Retail Banking on +233 302 661701 - 10</p>
            </div>
            
        
    </div>
</body>
{% endfor %}
</html>
'''

def save_statement_to_html(state_temp,visitor_folder, transactions, opening_balance, closing_balance, first_transaction_date, firstname, lastname, branch, staffid, acc, date_printed, sal, opening_balance_original,total_debits,total_credits,addresss,mycity):
    rendered_html = render_template_string(state_temp, 
                                           opening_balance=opening_balance, 
                                           closing_balance=closing_balance, 
                                           transactions=transactions,
                                           firstname=firstname,
                                           lastname=lastname,
                                           branch=branch,
                                           staffid=staffid, 
                                           first_transaction_date=first_transaction_date,
                                           acc=acc,
                                           date_printed=date_printed,
                                           sal=sal,
                                           start_balance=opening_balance_original,
                                           total_debits=total_debits,
                                           total_credits=total_credits,
                                           addresss=addresss,
                                           mycity=mycity)
    with open(os.path.join(visitor_folder, 'statement.html'), 'w') as file:
        file.write(rendered_html)
