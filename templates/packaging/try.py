from flask import Flask, render_template
from datetime import datetime, timedelta
import random

app = Flask(__name__)

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

@app.route('/')
def index():
    closing_balance = 100000  # Initial balance
    num_transactions = 20     # Number of transactions
    transactions = generate_transactions(closing_balance, num_transactions)
    return render_template('bank_statement.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)
