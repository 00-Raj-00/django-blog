# Django Blog

A full-stack blog web application built with **Python and Django**.
The project allows users to register/login, publish articles with images, browse blog posts, and manage content through Django's authentication and administration features.

## 🚀 Features

* User registration and authentication
* Login and logout functionality
* Create and publish blog articles
* Upload article images
* Article title, introduction, body and conclusion
* Author association with articles
* Automatic article creation date
* Blog post pagination
* Django Admin panel
* Static file configuration
* Media/image file handling
* SQLite database for development
* Production-ready project structure
* Deployed Django application

## 🛠️ Tech Stack

### Backend

* Python
* Django 6.0.5
* Django REST Framework

### Database

* SQLite

### Frontend

* HTML
* CSS
* Django Templates

### Other

* Git
* GitHub
* Virtual Environment
* Production deployment configuration

## 📁 Project Structure

```text
project/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── media/
│
└── static/
```

> Folder names may differ depending on the final project configuration.

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd <project-directory>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🗄️ Database Setup

Run Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the terminal instructions to create the admin user.

## ▶️ Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The Django Admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

## 🔐 Authentication

The application includes user authentication functionality.

Users can:

* Register an account
* Login
* Logout
* Access authenticated functionality
* Associate published articles with their account

Django's authentication system is used to manage login sessions and authentication.

## 📝 Blog Articles

Each article contains information such as:

* Title
* Introduction
* Body/content
* Conclusion
* Author
* Image
* Creation date

Articles are associated with their author and can be displayed through the blog interface.

## 🖼️ Image Upload

The project supports image uploads for blog articles.

Uploaded files are handled using Django's media configuration.

Example configuration:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

During development, media files are served through Django's development configuration.

For production deployment, media files should preferably be stored using dedicated object/file storage.

## 📄 Pagination

Blog articles are displayed using Django's `Paginator`.

This prevents all articles from being loaded and displayed on a single page.

Example:

```python
from django.core.paginator import Paginator

paginator = Paginator(articles, 5)
page_number = request.GET.get("page")
page_obj = paginator.get_page(page_number)
```

Pagination provides navigation between different pages of articles.

## 🗃️ Static Files

Static files such as CSS, JavaScript and other frontend assets are managed using Django's static file system.

Typical configuration:

```python
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```

Before production deployment:

```bash
python manage.py collectstatic
```

## 🔧 Environment Variables

Sensitive configuration should not be committed to GitHub.

For production, values such as the following should be stored as environment variables:

```text
SECRET_KEY
DEBUG
DATABASE_URL
ALLOWED_HOSTS
```

Never commit passwords, secret keys, API keys or other credentials to the repository.

## 📦 Requirements

The project dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

Generate/update the requirements file when necessary:

```bash
pip freeze > requirements.txt
```

## 🚀 Deployment

The project has been prepared for deployment using a production WSGI/ASGI configuration.

Before deploying, make sure to:

1. Set `DEBUG=False`
2. Configure `ALLOWED_HOSTS`
3. Configure production environment variables
4. Run database migrations
5. Run `collectstatic`
6. Configure static file serving
7. Configure media/file storage
8. Use a production server instead of Django's development server

Example:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

## 🔒 Security Considerations

For production deployment:

* Keep `SECRET_KEY` private
* Set `DEBUG=False`
* Configure `ALLOWED_HOSTS`
* Use HTTPS
* Do not commit `.env` files
* Protect database credentials
* Configure secure cookies
* Configure CSRF trusted origins when required
* Use proper production static/media storage

## 🧪 Development

To check the Django project for common configuration problems:

```bash
python manage.py check
```

Run migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

## 📌 Future Improvements

Possible improvements for future versions:

* Django REST Framework API
* User profile system
* Article editing and deletion
* Comments
* Likes
* Search functionality
* Categories and tags
* PostgreSQL production database
* Cloud media storage
* API authentication
* Automated tests
* CI/CD pipeline
* Docker support
* Better frontend UI

## 🎯 Learning Goals

This project was developed to gain practical experience with:

* Django project architecture
* Models and relationships
* Django ORM
* Forms
* Authentication
* Sessions
* CRUD operations
* File uploads
* Static and media files
* Pagination
* Django Admin
* REST APIs
* SQL/database concepts
* Git and GitHub
* Deployment

## 👨‍💻 Author

**Raj**

Python / Django Backend Developer

Currently pursuing **MCA** at **Maharaja Ranjit Singh Punjab Technical University**, with expected completion in **2027**.

---

⭐ If you find this project useful, consider giving the repository a star.
