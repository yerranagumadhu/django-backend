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

```
├── Backend/
│   ├── manage.py
│   ├── backend/                # Django project settings
│   ├── employees/              # Main app
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── templates/
│   ├── static/
│   └── templates/
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
