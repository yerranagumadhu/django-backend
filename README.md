# 🛠️ Django Backend Project

This is a Django-based backend application built for managing employee-related data including departments, job titles, projects, and performance reviews.

## 🚀 Features

- Full CRUD support for:
  - Employees
  - Departments
  - Job Titles
  - Projects
  - Performance Reviews
- API endpoints to fetch relational data (e.g., employee's department, projects, reviews)
- Admin panel integration
- PostgreSQL as the backend database
- Django REST Framework support for API

## 🗂️ Project Structure

# Django Employee Register with SAML Authentication

## Project Structure

```bash
project_name/
├── employee_register/                       # Main Django app for employee registration
│   ├── migrations/                          # Database migration files
│   ├── templates/                           # HTML files for rendering views
│   │   ├── employee_list.html               # Employee list page template
│   │   ├── logout_page.html                 # Custom logout page template
│   ├── __init__.py
│   ├── admin.py                             # Django admin panel configuration
│   ├── apps.py                              # Django app configuration
│   ├── models.py                            # Database models for employee data
│   ├── tests.py                             # Unit tests
│   ├── views.py                             # Views for handling the logic
│   ├── urls.py                              # URL routing for the employee app
│   ├── forms.py                             # Forms for handling user inputs (optional)
│   └── static/                              # Static files (CSS, JS, Images)
│       ├── css/                             # Stylesheets
│       ├── js/                              # JavaScript files (optional)
│       └── images/                          # Image files (optional)
├── saml_auth/                               # App handling SAML authentication
│   ├── __init__.py
│   ├── views.py                             # SAML authentication views (login, logout)
│   ├── urls.py                              # URL routing for SAML-related routes
│   ├── metadata.py                          # Metadata for the SAML authentication
│   ├── saml_settings.py                     # SAML settings (SP and IdP details)
├── employee/                                # Project directory (main root)
│   ├── OKTA/                                # Store Okta certificates or configuration here
│   │   └── okta.cert                        # Okta x509 certificate
│   ├── __init__.py
│   ├── manage.py                            # Django manage script
│   ├── settings.py                          # Django settings file
│   ├── urls.py                              # URL routing for the main project
│   ├── wsgi.py                              # WSGI configuration
│   └── asgi.py                              # ASGI configuration (for async support)
├── .gitignore                               # Git ignore file
├── requirements.txt                        # List of project dependencies
└── README.md                                # GitHub readme file
```

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/django-backend.git
cd django-backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Update `settings.py` with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

## 📬 API Example

Get detailed employee info:

```
GET /api/employees/<employee_id>/
```

Response:

```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "department": {
    "name": "Engineering",
    "location": "New York"
  },
  "job_title": {
    "title": "Senior Developer",
    "description": "Backend specialist"
  },
  ...
}
```

## 📄 License

This project is licensed under the MIT License.
