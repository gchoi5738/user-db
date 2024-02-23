# User Database Project

## Overview

This Django project focuses on creating a user database with essential fields such as First Name, Last Name, Email, Phone Number, Password, Order Status, and Connected Organization.

## Getting Started

### 1. Clone the Repository:

```bash
git clone https://github.com/gchoi5738/user-db.git
cd user-db
```
2. Setup Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install Dependencies:
```bash
pip install -r requirements.txt
```
4. Run Migrations:
```bash
python manage.py migrate
```
5. Create a Superuser:
```bash
python manage.py createsuperuser
```
6. Run the Development Server:
```bash
python manage.py runserver
```
Access the Django Admin Interface at http://127.0.0.1:8000/admin/ to manage user records.

Project Structure
user_management_app: Django app for user management


models.py: Defines the data models, including the User model. 


views.py: Handles views and logic related to user interactions. 


urls.py: Maps URLs to views within the app. 


Database: The project uses Django's default SQLite database for simplicity.

Usage
Create a New User: Navigate to http://127.0.0.1:8000/admin/ and log in with the superuser credentials. Create new users through the Django Admin Interface.
Customization
Add Fields: To add or modify fields in the user model, edit user_management_app/models.py.
Contributing
Feel free to contribute to the project by opening issues or submitting pull requests.

License
This project is licensed under the MIT License.