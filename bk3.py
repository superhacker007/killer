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
         "FEE- EBANKING ACH OUTWARD: TRAN ID -S"+ vul.generate_random_trans_id(6),
    ]
    debit_descriptions_above_100 = [
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "RTGS PMT 00000"+ ' ' +params['firstname'] + ' ' +params['lastname'],
        "TRANSACT HOME "+ ''.join([str(random.randint(0, 9)) for _ in range(17)]),
        "IB PMT-SISS 00000"+ vul.generate_random_trans_id(6)+ ' ' +vul.random_female_friend_firstname()+ ' ' +params['lastname'],
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
                "transaction_id":vul.generate_random_trans_id(11),
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
                "transaction_id":vul.generate_random_trans_id(11),
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