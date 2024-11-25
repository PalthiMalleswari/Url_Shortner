# Django URL Shortener  

A professional URL shortener application built with **Django**, **Python**, **HTML**, and **CSS**, designed to convert long URLs into compact, shareable links while providing efficient redirection to the original URLs.  

---

## Features  
- **Shorten Long URLs**: Convert lengthy URLs into short, user-friendly links.  
- **Redirection**: Automatically redirect users to the original URL when the short link is accessed.  
- **URL Validation**: Ensures that only valid URLs are accepted.  
- **Minimalistic UI**: Clean and responsive interface for seamless user experience.  

---

## Tech Stack  
- **Backend**: Django, Python  
- **Frontend**: HTML, CSS  

---

## Prerequisites  
- Python 3.8+  
- pip (Python package installer)  
- Django 4.0+  

---

## Setup Instructions  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/django-url-shortener.git
   cd django-url-shortener

2. **Create a Virtual Environment**

    ```bash
    Copy code
    python -m venv shortener_env  
    source shortener_env/bin/activate  # On Windows: shortener_env\Scripts\activate

3. **Install Dependencies**

    ```bash
    Copy code
    pip install -r requirements.txt

4. **Apply Migrations**

    ```bash
    Copy code
    python manage.py makemigrations  
    python manage.py migrate
5. **Run the Development Server**

    ```bash
    Copy code
    python manage.py runserver
    Access the Application
Open your browser and navigate to: http://127.0.0.1:8000/

