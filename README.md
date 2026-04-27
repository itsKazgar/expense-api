# Expense Tracker API 💸

A lightweight REST API built with Python and Flask for tracking personal expenses. Supports adding, retrieving, deleting expenses, and getting a spending summary broken down by category.

Built as a portfolio project to demonstrate backend development skills including REST API design, HTTP methods, JSON handling, and input validation.

---

## Features

- Add expenses with amount, description, and category
- Retrieve all expenses or filter by category
- Delete expenses by ID
- Get a spending summary with totals broken down by category
- Input validation with helpful error messages
- Clean JSON responses on every endpoint

---

## Requirements

- Python 3.6+
- Flask 3.1.3

---

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/expense-api.git
cd expense-api

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Running the API

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/expenses` | Get all expenses |
| GET | `/expenses?category=food` | Filter by category |
| POST | `/expenses` | Add a new expense |
| DELETE | `/expenses/<id>` | Delete an expense |
| GET | `/expenses/summary` | Get spending summary |

---

## Example Usage

**Add an expense:**
```bash
curl -X POST http://127.0.0.1:5000/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": 12.50, "description": "Lunch", "category": "food"}'
```

**Response:**
```json
{
  "id": 1,
  "amount": 12.50,
  "description": "Lunch",
  "category": "food",
  "date": "2024-11-20 14:32"
}
```

**Get all expenses:**
```bash
curl http://127.0.0.1:5000/expenses
```

**Filter by category:**
```bash
curl http://127.0.0.1:5000/expenses?category=food
```

**Get spending summary:**
```bash
curl http://127.0.0.1:5000/expenses/summary
```

**Response:**
```json
{
  "total": 71.49,
  "count": 3,
  "by_category": {
    "food": 21.49,
    "utilities": 50.00
  }
}
```

**Delete an expense:**
```bash
curl -X DELETE http://127.0.0.1:5000/expenses/1
```

---

## Project Structure

```
expense-api/
├── app.py            # Main application and all API routes
├── requirements.txt  # Python dependencies
├── README.md         # This file
├── .gitignore        # Files excluded from Git
└── LICENSE           # MIT License
```

---

## What I Learned

- Designing and building a REST API from scratch
- Using HTTP methods correctly (GET, POST, DELETE)
- Handling and validating JSON request data
- Returning appropriate HTTP status codes (200, 201, 400, 404)
- Using Python virtual environments professionally
- Structuring a Flask application cleanly

---

## Future Improvements

- Add a database (SQLite) for persistent storage
- Add a PUT endpoint to edit existing expenses
- Add user authentication
- Deploy to a cloud platform like Render or Railway

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
