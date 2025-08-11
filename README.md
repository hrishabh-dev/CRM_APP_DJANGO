# CRM_APP_DJANGO

A simple Customer Relationship Management (CRM) application built with Django.

## Overview

This project is a web-based CRM system that allows you to manage customer records efficiently. It is designed with Django and Bootstrap for a functional and clean user interface. The app supports authentication, registration, and all main CRUD operations for customer records.

> **Note:**  
> This is my first project! I am looking forward to building more advanced projects, including machine learning applications using Django.

## Features

- **User Authentication**: Secure login and registration system.
- **Customer Records Management**: Add, view, update, and delete customer details.
- **Record Details**: Store information like name, email, phone, address, city, state, zipcode, and creation date.
- **Admin Integration**: Django admin interface for backend management.
- **Bootstrap UI**: Responsive and styled templates with Bootstrap.

## Technologies Used

- Python
- Django
- Bootstrap

## Project Structure

```
CRM_APP_DJANGO/
├── dcrm/
│   ├── dcrm/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── website/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── navbar.html
│   │   │   ├── record.html
│   │   ├── views.py
│   ├── manage.py
├── venv/
│   └── (virtual environment files)
└── requirements.txt
```

- **dcrm/dcrm/**: Main Django project folder (settings, URLs, WSGI).
- **dcrm/website/**: Contains the CRM app (models, forms, views, templates).
- **dcrm/website/templates/**: HTML templates for the web interface.
- **venv/**: Python virtual environment.
- **requirements.txt**: Python dependencies.

## Getting Started

### Prerequisites

- Python (recommended 3.8+)
- Django (`pip install django`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hrishabh-dev/CRM_APP_DJANGO.git
   cd CRM_APP_DJANGO
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

6. **Access the app**
   - Main app: [http://localhost:8000/](http://localhost:8000/)
   - Admin panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Usage

- **Login/Register:** Use the navigation bar to log in or register a new user.
- **View Records:** View all customer records on the home page (after login).
- **Add Record:** Click "Add Record" in the navigation bar to add a new customer.
- **View/Update/Delete Record:** Click a record to view details, edit, or delete.

## Database Model

The main model is `Records`, which tracks:
- First name
- Last name
- Email
- Phone
- Address
- City
- State
- Zipcode
- Created at (timestamp)

## License

This project currently does not specify a license.

## Author

[hrishabh-dev](https://github.com/hrishabh-dev)
