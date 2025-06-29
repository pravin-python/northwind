# Northwind Django Project

This is a Django-based web application built using the Northwind sample database, often used for learning and demonstrating database operations in a business setting (customers, orders, products, etc.).

## 📂 Project Structure

- `apps/` – Contains modular Django apps for handling different business logic.
- `northwind/` – Main project folder with settings and URLs.
- `templates/` – HTML templates for rendering views.
- `static/` – Static files (CSS, JS, etc.).
- `db.sqlite3` – Default SQLite database used for local development.

## 💡 Features

- Customer management
- Product and order tracking
- Admin dashboard (Django Admin)
- Relational data modeling using Django ORM

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation

```bash
# Clone the repo
git clone https://github.com/pravin-python/northwind.git
cd northwind

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
