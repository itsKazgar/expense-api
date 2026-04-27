from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage (acts like a database for now)
expenses = []
next_id = 1


@app.route('/expenses', methods=['GET'])
def get_expenses():
    """Get all expenses, optionally filter by category."""
    category = request.args.get('category')
    if category:
        filtered = [e for e in expenses if e['category'].lower() == category.lower()]
        return jsonify(filtered)
    return jsonify(expenses)


@app.route('/expenses', methods=['POST'])
def add_expense():
    """Add a new expense."""
    global next_id
    data = request.get_json()

    # Validate required fields
    if not data or 'amount' not in data or 'description' not in data:
        return jsonify({'error': 'amount and description are required'}), 400

    if not isinstance(data['amount'], (int, float)) or data['amount'] <= 0:
        return jsonify({'error': 'amount must be a positive number'}), 400

    expense = {
        'id': next_id,
        'amount': round(data['amount'], 2),
        'description': data['description'],
        'category': data.get('category', 'general'),
        'date': datetime.now().strftime('%Y-%m-%d %H:%M')
    }

    expenses.append(expense)
    next_id += 1
    return jsonify(expense), 201


@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    """Delete an expense by ID."""
    global expenses
    original_count = len(expenses)
    expenses = [e for e in expenses if e['id'] != expense_id]

    if len(expenses) == original_count:
        return jsonify({'error': f'Expense {expense_id} not found'}), 404

    return jsonify({'message': f'Expense {expense_id} deleted'}), 200


@app.route('/expenses/summary', methods=['GET'])
def get_summary():
    """Get total spending and breakdown by category."""
    if not expenses:
        return jsonify({'total': 0, 'by_category': {}, 'count': 0})

    total = sum(e['amount'] for e in expenses)
    by_category = {}
    for e in expenses:
        cat = e['category']
        by_category[cat] = round(by_category.get(cat, 0) + e['amount'], 2)

    return jsonify({
        'total': round(total, 2),
        'count': len(expenses),
        'by_category': by_category
    })


if __name__ == '__main__':
    app.run(debug=True)
