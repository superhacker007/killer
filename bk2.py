import random
import pandas as pd
import numpy as np
import vul  # Assuming this module contains the necessary functions

def generate_random_transactions_adb(params, initial_balance, salary_amount):
    # Get today's date
    today = pd.to_datetime("today").normalize()
    
    # Adjust today to the previous business day if it is not a business day
    if not np.is_busday(today.strftime('%Y-%m-%d')):
        end_date = pd.to_datetime(np.busday_offset(today.strftime('%Y-%m-%d'), 0, roll='backward'))
    else:
        end_date = today

    # Set the start date to 4 months ago
    start_date = end_date - pd.DateOffset(months=4)
    all_days = pd.date_range(start_date, end_date).tolist()  # Include all days, not just business days
    transaction_types = ['debit', 'credit']
    
    # Descriptions separated by type and amount
    debit_descriptions_below_100 = [
         "FEE RTGS 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
         "FEE- EBANKING ACH OUTWARD: TRAN ID -S"+ vul.generate_random_string(6),
    ]
    debit_descriptions_above_100 = [
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "TRANSACT HOME "+ ''.join([str(random.randint(0, 9)) for _ in range(17)]),
        "IB PMT-SISS 00000"+ vul.generate_random_string(6)+ ' ' +vul.random_female_friend_firstname()+ ' ' +params['lastname'],
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        vul.generate_random_name()+" "+vul.generate_random_string(7),
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:],
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:],
    ]
    credit_descriptions = [
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        vul.generate_random_name()+" "+vul.generate_random_string(7),
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:],
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:],
    ]
    
    transactions = []
    balance = initial_balance

    total_debits = 0
    total_credits = 0
    num_debit_transactions = 0
    num_credit_transactions = 0

    opening_balance = initial_balance

    # Helper functions to get random descriptions
    def get_debit_description(amount):
        if amount < 100:
            return random.choice(debit_descriptions_below_100)
        else:
            return random.choice(debit_descriptions_above_100)

    def get_credit_description():
        return random.choice(credit_descriptions)

    # Adding the opening balance
    transactions.append({
        "transaction_date": start_date.strftime("%d-%m-%Y"),
        "value_date": start_date.strftime("%d-%m-%Y"),
        "description": "STATEMENT OPENING BALANCE",
        "fee": "",
        "debit": "",
        "credit": "",
        "balance": f"{balance:,.2f}"
    })

    for date in all_days:
        # Randomly decide to generate a transaction or not
        if random.choice([True, False]):
            transaction_type = random.choice(transaction_types)
            debit_amount = round(random.randint(1, 500)*10, 2)
            credit_amount = round(random.randint(1, 1000)*10, 2)

            if transaction_type == 'debit':
                description = get_debit_description(debit_amount)
                debit = debit_amount
                credit = 0.00
                balance -= debit
                total_debits += debit
                num_debit_transactions += 1
            else:
                description = get_credit_description()
                debit = 0.00
                credit = credit_amount
                balance += credit
                total_credits += credit
                num_credit_transactions += 1

            transactions.append({
                "transaction_date": date.strftime("%d-%m-%Y"),
                "value_date": date.strftime("%d-%m-%Y"),
                "description": description,
                "transaction_id":vul.generate_random_string(11),
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '0.00',
                "credit": f"{credit:,.2f}" if credit else '0.00',
                "balance": f"{balance:,.2f}"
            })

        # Add a salary transaction at the end of the month
        if date == all_days[-1] or (date.month != all_days[all_days.index(date) + 1].month):
            salary_date = date
            description = (params['employer']+"SAL"+salary_date.strftime("%b")+salary_date.strftime("%Y")+" PAYEX-"+''.join([str(random.randint(0, 9)) for _ in range(14)])).upper()
            debit = 0
            credit = salary_amount
            balance += credit
            total_credits += credit
            num_credit_transactions += 1
            transactions.append({
                "transaction_date": salary_date.strftime("%d-%m-%Y"),
                "value_date": salary_date.strftime("%d-%m-%Y"),
                "description": description,
                "transaction_id":vul.generate_random_string(11),
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '0.00',
                "credit": f"{credit:,.2f}" if credit else '0.00',
                "balance": f"{balance:,.2f}"
            })

    closing_balance = balance

    result_summary = {
        "total_debits": f"{total_debits:,.2f}",
        "total_credits": f"{total_credits:,.2f}",
        "num_debit_transactions": num_debit_transactions,
        "num_credit_transactions": num_credit_transactions,
        "first_transaction_date": transactions[0]["transaction_date"] if transactions else "",
        "last_transaction_date": transactions[-1]["transaction_date"] if transactions else "",
        "opening_balance": f"{opening_balance:,.2f}",
        "closing_balance": f"{closing_balance:,.2f}"
    }

    return transactions, result_summary

def generate_random_transactions_gcb(params, initial_balance, salary_amount):
    # Get today's date
    today = pd.to_datetime("today").normalize()
    
    # Adjust today to the previous business day if it is not a business day
    if not np.is_busday(today.strftime('%Y-%m-%d')):
        end_date = pd.to_datetime(np.busday_offset(today.strftime('%Y-%m-%d'), 0, roll='backward'))
    else:
        end_date = today

    # Set the start date to 4 months ago
    start_date = end_date - pd.DateOffset(months=4)
    all_days = pd.date_range(start_date, end_date).tolist()  # Include all days, not just business days
    transaction_types = ['debit', 'credit']
    
    # Descriptions separated by type and amount
    debit_descriptions_below_100 = [
         "FEE RTGS 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
         "FEE- EBANKING ACH OUTWARD: TRAN ID -S"+ vul.generate_random_string(6),
    ]
    debit_descriptions_above_100 = [
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "TRANSACT HOME "+ ''.join([str(random.randint(0, 9)) for _ in range(17)]),
        "IB PMT-SISS 00000"+ vul.generate_random_string(6)+ ' ' +vul.random_female_friend_firstname()+ ' ' +params['lastname'],
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:],
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:],
    ]
    credit_descriptions = [
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:],
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:],
        "CASH DEPOSIT BY "+params['firstname'] + ' ' +params['lastname'],
        "CASH DEPOSIT BY "+params['firstname'] + ' ' +params['lastname'],
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
    ]
    
    transactions = []
    balance = initial_balance

    total_debits = 0
    total_credits = 0
    num_debit_transactions = 0
    num_credit_transactions = 0

    opening_balance = initial_balance

    # Helper functions to get random descriptions
    def get_debit_description(amount):
        if amount < 100:
            return random.choice(debit_descriptions_below_100)
        else:
            return random.choice(debit_descriptions_above_100)

    def get_credit_description():
        return random.choice(credit_descriptions)

    for date in all_days:
        # Randomly decide to generate a transaction or not
        if random.choice([True, False]):
            transaction_type = random.choice(transaction_types)
            debit_amount = round(random.randint(1, 500) * 10, 2)
            credit_amount = round(random.randint(1, 1000) * 10, 2)

            if transaction_type == 'debit':
                description = get_debit_description(debit_amount)
                transaction_id = vul.generate_random_string(15)
                debit = debit_amount
                credit = ''
                balance -= debit
                total_debits += debit
                num_debit_transactions += 1
            else:
                description = get_credit_description()
                transaction_id = vul.generate_random_string(15)
                debit = ''
                credit = credit_amount
                balance += credit
                total_credits += credit
                num_credit_transactions += 1

            transactions.append({
                "transaction_date": date.strftime('%d-%b-%Y'),
                "value_date": date.strftime('%d-%b-%Y'),
                "description": description,
                "transaction_id": transaction_id,
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '',
                "credit": f"{credit:,.2f}" if credit else '',
                "balance": f"{balance:,.2f}"
            })

        # Add a salary transaction on the 24th of each month
        if date.day == 24:
            salary_date = date
            description = (params['employer'] + "SAL" + salary_date.strftime("%b") + salary_date.strftime("%Y") + " PAYEX-" + ''.join([str(random.randint(0, 9)) for _ in range(14)])).upper()
            debit = 0
            credit = salary_amount
            balance += credit
            total_credits += credit
            num_credit_transactions += 1
            transactions.append({
                "transaction_date": salary_date.strftime('%d-%b-%Y'),
                "value_date": salary_date.strftime('%d-%b-%Y'),
                "description": description,
                "transaction_id": vul.generate_random_trans_id(15),
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '',
                "credit": f"{credit:,.2f}" if credit else '',
                "balance": f"{balance:,.2f}"
            })

    # Add a specific debit transaction of 500 one week ago
    # if params['conference'] == 'yes':
    #     one_week_ago = today - pd.DateOffset(weeks=1)
    #     description = "POS PURCHASE GLOBAL CONFERENCE ALLIANCE" + vul.generate_random_string(10)
    #     debit = 500
    #     credit = ''
    #     balance -= debit
    #     total_debits += debit
    #     num_debit_transactions += 1
    #     transactions.append({
    #         "transaction_date": one_week_ago.strftime('%d-%b-%Y'),
    #         "value_date": one_week_ago.strftime('%d-%b-%Y'),
    #         "description": description,
    #         "transaction_id": vul.generate_random_string(15),
    #         "fee": "",
    #         "debit": f"{debit:,.2f}" if debit else '',
    #         "credit": f"{credit:,.2f}" if credit else '',
    #         "balance": f"{balance:,.2f}"
    #     })

    closing_balance = balance

    result_summary = {
        "total_debits": f"{total_debits:,.2f}",
        "total_credits": f"{total_credits:,.2f}",
        "num_debit_transactions": num_debit_transactions,
        "num_credit_transactions": num_credit_transactions,
        "first_transaction_date": transactions[0]["transaction_date"] if transactions else "",
        "last_transaction_date": transactions[-1]["transaction_date"] if transactions else "",
        "opening_balance": f"{opening_balance:,.2f}",
        "closing_balance": f"{closing_balance:,.2f}"
    }

    return transactions, result_summary

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
                {"short": "Transfer", "long": f"{branch} BRANCH: CHEQUE DEPOSIT; CHEQ BY {random.choice(vul.first_female_names).upper()} {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"}
            ]
    return random.choice(descriptions)

def generate_detailed_description_school(is_debit, acc, amount, firstname, lastname, branch, staffid, phonen, mycity, network, bank2):
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
                {"short": "Transfer", "long": f"{branch} BRANCH: ACCOUNT TO WALLET; FBGMA NSANO CREDIT FROM AC {acc} TO {network} {phonen}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: INTER BANK TRANSFER; FBGMA NSANO CREDIT FROM AC {acc} TO {bank2} LTD; {lastname}"},
            ]
        else:
            descriptions = [
                {"short": "Transfer", "long": f"{branch} BRANCH: INTER BANK TRANSFER; FBGMA NSANO CREDIT FROM AC {acc} TO {bank2} LTD; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: INTER BANK TRANSFER; FBGMA NSANO CREDIT FROM AC {acc} TO {bank2} LTD; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: INTER BANK TRANSFER; FBGMA NSANO CREDIT FROM AC {acc} TO {bank2} LTD; {lastname}"},
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
                {"short": "Transfer", "long": f"{branch} BRANCH: CHEQUE DEPOSIT; CHEQ BY {random.choice(vul.first_female_names).upper()} {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"},
                {"short": "Transfer", "long": f"{branch} BRANCH: WALLET TO ACCOUNT; FBGMA NSANO MOMO FROM NO. {phonen} TO ACC {acc}; {lastname}"}
            ]
    return random.choice(descriptions)

def generate_random_transactions_nib_school(params, initial_balance, salary_amount):

    
    # Get today's date
    today = pd.to_datetime("today").normalize()
    
    # Adjust today to the previous business day if it is not a business day
    if not np.is_busday(today.strftime('%Y-%m-%d')):
        end_date = pd.to_datetime(np.busday_offset(today.strftime('%Y-%m-%d'), 0, roll='backward'))
    else:
        end_date = today

    # Set the start date to 4 months ago
    start_date = end_date - pd.DateOffset(months=4)
    all_days = pd.date_range(start_date, end_date).tolist()  # Include all days, not just business days
    transaction_types = ['debit', 'credit']
    
    transactions = []
    balance = initial_balance

    total_debits = 0
    total_credits = 0
    num_debit_transactions = 0
    num_credit_transactions = 0

    opening_balance = initial_balance

    for date in all_days:
        # Randomly decide to generate a transaction or not
        if random.choice([True, False]):
            transaction_type = random.choice(transaction_types)
            debit_amount = round(random.randint(1, 500) * 10, 2)
            credit_amount = round(random.randint(1, 1000) * 10, 2)

            if transaction_type == 'debit':
                description = generate_detailed_description_school(True, params['acc'], debit_amount, params['firstname'], params['lastname'], params['branch'], params['staffid'], params['phonen'], params['mycity'], params['network'], params['bank2'])
                short_description = description["short"]
                long_description = description["long"]
                transaction_id = vul.generate_random_string(15)
                debit = debit_amount
                credit = ''
                balance -= debit
                total_debits += debit
                num_debit_transactions += 1
            else:
                description = generate_detailed_description_school(False, params['acc'], credit_amount, params['firstname'], params['lastname'], params['branch'], params['staffid'], params['phonen'], params['mycity'], params['network'], params['bank2'])
                short_description = description["short"]
                long_description = description["long"]
                transaction_id = vul.generate_random_string(15)
                debit = ''
                credit = credit_amount
                balance += credit
                total_credits += credit
                num_credit_transactions += 1

            transactions.append({
                "transaction_date": date.strftime('%d-%b-%Y'),
                "value_date": date.strftime('%d-%b-%Y'),
                "description": short_description,
                "details": long_description,
                "transaction_id": transaction_id,
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '',
                "credit": f"{credit:,.2f}" if credit else '',
                "balance": f"{balance:,.2f}"
            })

        # Add a salary transaction on the 24th of each month
        if params['hassal'] == '1':
            if date.day == 24:
                salary_date = date
                description = params['employer'] + "HEAD OFFICE SALARY PROCESSING " + salary_date.strftime("%b") + salary_date.strftime("%Y") + " SAL PAYMNT B/O CAG "
                debit = 0
                credit = salary_amount
                balance += credit
                total_credits += credit
                num_credit_transactions += 1
                transactions.append({
                    "transaction_date": salary_date.strftime('%d-%b-%Y'),
                    "value_date": salary_date.strftime('%d-%b-%Y'),
                    "description": 'SALARY',
                    "details": description,
                    "transaction_id": vul.generate_random_trans_id(15),
                    "fee": "",
                    "debit": f"{debit:,.2f}" if debit else '',
                    "credit": f"{credit:,.2f}" if credit else '',
                    "balance": f"{balance:,.2f}"
                })

    closing_balance = balance

    result_summary = {
        "total_debits": f"{total_debits:,.2f}",
        "total_credits": f"{total_credits:,.2f}",
        "num_debit_transactions": num_debit_transactions,
        "num_credit_transactions": num_credit_transactions,
        "first_transaction_date": transactions[0]["transaction_date"] if transactions else "",
        "last_transaction_date": transactions[-1]["transaction_date"] if transactions else "",
        "opening_balance": f"{opening_balance:,.2f}",
        "closing_balance": f"{closing_balance:,.2f}"
    }

    return transactions, result_summary

def generate_random_transactions_nib(params, initial_balance, salary_amount):

    
    # Get today's date
    today = pd.to_datetime("today").normalize()
    
    # Adjust today to the previous business day if it is not a business day
    if not np.is_busday(today.strftime('%Y-%m-%d')):
        end_date = pd.to_datetime(np.busday_offset(today.strftime('%Y-%m-%d'), 0, roll='backward'))
    else:
        end_date = today

    # Set the start date to 4 months ago
    start_date = end_date - pd.DateOffset(months=4)
    all_days = pd.date_range(start_date, end_date).tolist()  # Include all days, not just business days
    transaction_types = ['debit', 'credit']
    
    transactions = []
    balance = initial_balance

    total_debits = 0
    total_credits = 0
    num_debit_transactions = 0
    num_credit_transactions = 0

    opening_balance = initial_balance

    for date in all_days:
        # Randomly decide to generate a transaction or not
        if random.choice([True, False]):
            transaction_type = random.choice(transaction_types)
            debit_amount = round(random.randint(1, 500) * 10, 2)
            credit_amount = round(random.randint(1, 1000) * 10, 2)

            if transaction_type == 'debit':
                description = generate_detailed_description(True, params['acc'], debit_amount, params['firstname'], params['lastname'], params['branch'], params['staffid'], params['phonen'], params['mycity'], params['network'])
                short_description = description["short"]
                long_description = description["long"]
                transaction_id = vul.generate_random_string(15)
                debit = debit_amount
                credit = ''
                balance -= debit
                total_debits += debit
                num_debit_transactions += 1
            else:
                description = generate_detailed_description(False, params['acc'], credit_amount, params['firstname'], params['lastname'], params['branch'], params['staffid'], params['phonen'], params['mycity'], params['network'])
                short_description = description["short"]
                long_description = description["long"]
                transaction_id = vul.generate_random_string(15)
                debit = ''
                credit = credit_amount
                balance += credit
                total_credits += credit
                num_credit_transactions += 1

            transactions.append({
                "transaction_date": date.strftime('%d-%b-%Y'),
                "value_date": date.strftime('%d-%b-%Y'),
                "description": short_description,
                "details": long_description,
                "transaction_id": transaction_id,
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '',
                "credit": f"{credit:,.2f}" if credit else '',
                "balance": f"{balance:,.2f}"
            })

        # Add a salary transaction on the 24th of each month
        if params['hassal'] == '1':
            if date.day == 24:
                salary_date = date
                description = params['employer'] + "HEAD OFFICE SALARY PROCESSING " + salary_date.strftime("%b") + salary_date.strftime("%Y") + " SAL PAYMNT B/O CAG "
                debit = 0
                credit = salary_amount
                balance += credit
                total_credits += credit
                num_credit_transactions += 1
                transactions.append({
                    "transaction_date": salary_date.strftime('%d-%b-%Y'),
                    "value_date": salary_date.strftime('%d-%b-%Y'),
                    "description": 'SALARY',
                    "details": description,
                    "transaction_id": vul.generate_random_trans_id(15),
                    "fee": "",
                    "debit": f"{debit:,.2f}" if debit else '',
                    "credit": f"{credit:,.2f}" if credit else '',
                    "balance": f"{balance:,.2f}"
                })

    # Add a specific debit transaction of 500 one week ago
    # if params['conference'] == 'yes':
    #     one_week_ago = today - pd.DateOffset(weeks=1)
    #     description = "POS PURCHASE GLOBAL CONFERENCE ALLIANCE" + vul.generate_random_string(10)
    #     debit = 500
    #     credit = ''
    #     balance -= debit
    #     total_debits += debit
    #     num_debit_transactions += 1
    #     transactions.append({
    #         "transaction_date": one_week_ago.strftime('%d-%b-%Y'),
    #         "value_date": one_week_ago.strftime('%d-%b-%Y'),
    #         "description": description,
    #         "transaction_id": vul.generate_random_string(15),
    #         "fee": "",
    #         "debit": f"{debit:,.2f}" if debit else '',
    #         "credit": f"{credit:,.2f}" if credit else '',
    #         "balance": f"{balance:,.2f}"
    #     })

    closing_balance = balance

    result_summary = {
        "total_debits": f"{total_debits:,.2f}",
        "total_credits": f"{total_credits:,.2f}",
        "num_debit_transactions": num_debit_transactions,
        "num_credit_transactions": num_credit_transactions,
        "first_transaction_date": transactions[0]["transaction_date"] if transactions else "",
        "last_transaction_date": transactions[-1]["transaction_date"] if transactions else "",
        "opening_balance": f"{opening_balance:,.2f}",
        "closing_balance": f"{closing_balance:,.2f}"
    }

    return transactions, result_summary


def generate_random_transactions_gcb_toson(params, initial_balance, salary_amount, toson):
    # Get today's date
    today = pd.to_datetime("today").normalize()
    
    # Adjust today to the previous business day if it is not a business day
    if not np.is_busday(today.strftime('%Y-%m-%d')):
        end_date = pd.to_datetime(np.busday_offset(today.strftime('%Y-%m-%d'), 0, roll='backward'))
    else:
        end_date = today

    # Set the start date to 4 months ago
    start_date = end_date - pd.DateOffset(months=4)
    all_days = pd.date_range(start_date, end_date).tolist()  # Include all days, not just business days
    transaction_types = ['debit', 'credit']
    
    # Descriptions separated by type and amount
    debit_descriptions_below_100 = [
         "FEE RTGS 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
         "FEE- EBANKING ACH OUTWARD: TRAN ID -S"+ vul.generate_random_string(6),
    ]
    debit_descriptions_above_100 = [
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "TRANSACT HOME "+ ''.join([str(random.randint(0, 9)) for _ in range(17)]),
        "IB PMT-SISS 00000"+ vul.generate_random_string(6)+ ' ' +vul.random_female_friend_firstname()+ ' ' +params['lastname'],
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:] ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:],
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:],
    ]
    credit_descriptions = [
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] ,
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:],
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:],
        "CASH DEPOSIT BY "+params['firstname'] + ' ' +params['lastname'],
        "CASH DEPOSIT BY "+params['firstname'] + ' ' +params['lastname'],
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
        "CASH DEPOSIT BY SELF",
    ]
    
    transactions = []
    balance = initial_balance

    total_debits = 0
    total_credits = 0
    num_debit_transactions = 0
    num_credit_transactions = 0

    opening_balance = initial_balance

    # Helper functions to get random descriptions
    def get_debit_description(amount):
        if amount < 100:
            return random.choice(debit_descriptions_below_100)
        else:
            return random.choice(debit_descriptions_above_100)

    def get_credit_description():
        return random.choice(credit_descriptions)

    for date in all_days:
        # Randomly decide to generate a transaction or not
        if random.choice([True, False]):
            transaction_type = random.choice(transaction_types)
            debit_amount = round(random.randint(1, 500) * 10, 2)
            credit_amount = round(random.randint(1, 1000) * 10, 2)

            if transaction_type == 'debit':
                description = get_debit_description(debit_amount)
                transaction_id = vul.generate_random_string(15)
                debit = debit_amount
                credit = ''
                balance -= debit
                total_debits += debit
                num_debit_transactions += 1
            else:
                description = get_credit_description()
                transaction_id = vul.generate_random_string(15)
                debit = ''
                credit = credit_amount
                balance += credit
                total_credits += credit
                num_credit_transactions += 1

            transactions.append({
                "transaction_date": date.strftime('%d-%b-%Y'),
                "value_date": date.strftime('%d-%b-%Y'),
                "description": description,
                "transaction_id": transaction_id,
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '',
                "credit": f"{credit:,.2f}" if credit else '',
                "balance": f"{balance:,.2f}"
            })

        # Add a salary transaction on the 24th of each month
        if date.day == 24:
            salary_date = date
            description = (params['employer'] + "SAL" + salary_date.strftime("%b") + salary_date.strftime("%Y") + " PAYEX-" + ''.join([str(random.randint(0, 9)) for _ in range(14)])).upper()
            debit = 0
            credit = salary_amount
            balance += credit
            total_credits += credit
            num_credit_transactions += 1
            transactions.append({
                "transaction_date": salary_date.strftime('%d-%b-%Y'),
                "value_date": salary_date.strftime('%d-%b-%Y'),
                "description": description,
                "transaction_id": vul.generate_random_trans_id(15),
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '',
                "credit": f"{credit:,.2f}" if credit else '',
                "balance": f"{balance:,.2f}"
            })

    # Add the debit transaction with amount 'toson' as the very last transaction
    last_transaction_date = transactions[-1]["transaction_date"] if transactions else end_date.strftime('%d-%b-%Y')
    description = "CANADA TOUR FUNDS " + params['firstname'] + ' ' + params['lastname']
    balance -= toson
    total_debits += toson
    num_debit_transactions += 1

    transactions.append({
        "transaction_date": last_transaction_date,
        "value_date": last_transaction_date,
        "description": description,
        "transaction_id": vul.generate_random_string(15),
        "fee": "",
        "debit": f"{toson:,.2f}",
        "credit": '',
        "balance": f"{balance:,.2f}"
    })

    closing_balance = balance

    result_summary = {
        "total_debits": f"{total_debits:,.2f}",
        "total_credits": f"{total_credits:,.2f}",
        "num_debit_transactions": num_debit_transactions,
        "num_credit_transactions": num_credit_transactions,
        "first_transaction_date": transactions[0]["transaction_date"] if transactions else "",
        "last_transaction_date": transactions[-1]["transaction_date"] if transactions else "",
        "opening_balance": f"{opening_balance:,.2f}",
        "closing_balance": f"{closing_balance:,.2f}"
    }

    return transactions, result_summary



def generate_random_transactions(params, initial_balance, salary_amount):
    # Get today's date
    today = pd.to_datetime("today").normalize()
    
    # Adjust today to the previous business day if it is not a business day
    if not np.is_busday(today.strftime('%Y-%m-%d')):
        end_date = pd.to_datetime(np.busday_offset(today.strftime('%Y-%m-%d'), 0, roll='backward'))
    else:
        end_date = today

    # Set the start date to 4 months ago
    start_date = end_date - pd.DateOffset(months=4)
    all_days = pd.date_range(start_date, end_date).tolist()  # Include all days, not just business days
    transaction_types = ['debit', 'credit']
    
    # Descriptions separated by type and amount
    debit_descriptions_below_100 = [
         "FEE RTGS 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'] + ' ' +vul.generate_random_string(11),
         "FEE- EBANKING ACH OUTWARD: TRAN ID -S"+ vul.generate_random_trans_id(6),
    ]
    debit_descriptions_above_100 = [
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname']+ ' ' +vul.generate_random_string(11),
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname']+ ' ' +vul.generate_random_string(11),
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname']+ ' ' +vul.generate_random_string(11),
        "TRANSACT HOME "+ ''.join([str(random.randint(0, 9)) for _ in range(17)]),
        "IB PMT-SISS 00000"+ vul.generate_random_trans_id(6)+ ' ' +vul.random_female_friend_firstname()+ ' ' +params['lastname']+ ' ' +vul.generate_random_string(11),
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:]+ ' ' +vul.generate_random_string(11) ,
        vul.generate_random_name()+" "+vul.generate_random_string(7),
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:]+ ' ' +vul.generate_random_string(11) ,
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:]+ ' ' +vul.generate_random_string(11),
        "BANK2WALLET "+params['network']+" "+params['phonen'][1:]+ ' ' +vul.generate_random_string(11),
    ]
    credit_descriptions = [
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:]+ ' ' +vul.generate_random_string(11) ,
        vul.generate_random_name()+" "+vul.generate_random_string(7),
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] + ' ' +vul.generate_random_string(11),
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:] + ' ' +vul.generate_random_string(11),
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:]+ ' ' +vul.generate_random_string(11),
        "WALLETTOBANK "+params['network']+" "+params['phonen'][1:]+ ' ' +vul.generate_random_string(11),
    ]
    
    transactions = []
    balance = initial_balance

    total_debits = 0
    total_credits = 0
    num_debit_transactions = 0
    num_credit_transactions = 0

    opening_balance = initial_balance

    # Helper functions to get random descriptions
    def get_debit_description(amount):
        if amount < 100:
            return random.choice(debit_descriptions_below_100)
        else:
            return random.choice(debit_descriptions_above_100)

    def get_credit_description():
        return random.choice(credit_descriptions)

    # Adding the opening balance
    transactions.append({
        "transaction_date": start_date.strftime("%d-%m-%Y"),
        "value_date": start_date.strftime("%d-%m-%Y"),
        "description": "STATEMENT OPENING BALANCE",
        "fee": "",
        "debit": "",
        "credit": "",
        "balance": f"{balance:,.2f}"
    })

    # Calculate the date 3 weeks ago
    three_weeks_ago = today - pd.DateOffset(weeks=3)

    for date in all_days:
        # Check if the current date is 3 weeks ago
        if date == three_weeks_ago and 'conference' in params and params['conference'] == 'yes':
            specific_debit_amount = 8000
            balance -= specific_debit_amount
            total_debits += specific_debit_amount
            num_debit_transactions += 1
            transactions.append({
                "transaction_date": date.strftime("%d-%m-%Y"),
                "value_date": date.strftime("%d-%m-%Y"),
                "description": 'GLOBAL CONFERENCE ALLIANCE INC ' + vul.generate_random_string(10),
                "fee": "",
                "debit": f"{specific_debit_amount:,.2f}",
                "credit": "",
                "balance": f"{balance:,.2f}"
            })
        else:
            # Randomly decide to generate a transaction or not
            if random.choice([True, False]):
                transaction_type = random.choice(transaction_types)
                debit_amount = round(random.randint(1, 500) * 10, 2)
                credit_amount = round(random.randint(1, 1000) * 10, 2)

                if transaction_type == 'debit':
                    description = get_debit_description(debit_amount)
                    debit = debit_amount
                    credit = ''
                    balance -= debit
                    total_debits += debit
                    num_debit_transactions += 1
                else:
                    description = get_credit_description()
                    debit = ''
                    credit = credit_amount
                    balance += credit
                    total_credits += credit
                    num_credit_transactions += 1

                transactions.append({
                    "transaction_date": date.strftime("%d-%m-%Y"),
                    "value_date": date.strftime("%d-%m-%Y"),
                    "description": description,
                    "fee": "",
                    "debit": f"{debit:,.2f}" if debit else '',
                    "credit": f"{credit:,.2f}" if credit else '',
                    "balance": f"{balance:,.2f}"
                })

        # Add a salary transaction at the end of the month
        if date == all_days[-1] or (date.month != all_days[all_days.index(date) + 1].month):
            salary_date = date
            description = (params['employer'] + "SAL" + salary_date.strftime("%b") + salary_date.strftime("%Y") + " A. ADU ENTERPRISE-" + ''.join([str(random.randint(0, 9)) for _ in range(14)])).upper()
            debit = 0
            credit = salary_amount
            balance += credit
            total_credits += credit
            num_credit_transactions += 1
            transactions.append({
                "transaction_date": salary_date.strftime("%d-%m-%Y"),
                "value_date": salary_date.strftime("%d-%m-%Y"),
                "description": description,
                "fee": "",
                "debit": f"{debit:,.2f}" if debit else '',
                "credit": f"{credit:,.2f}" if credit else '',
                "balance": f"{balance:,.2f}"
            })

    closing_balance = balance

    result_summary = {
        "total_debits": f"{total_debits:,.2f}",
        "total_credits": f"{total_credits:,.2f}",
        "num_debit_transactions": num_debit_transactions,
        "num_credit_transactions": num_credit_transactions,
        "first_transaction_date": transactions[0]["transaction_date"] if transactions else "",
        "last_transaction_date": transactions[-1]["transaction_date"] if transactions else "",
        "opening_balance": f"{opening_balance:,.2f}",
        "closing_balance": f"{closing_balance:,.2f}"
    }

    return transactions, result_summary



