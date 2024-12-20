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
## Demo
[video](https://youtu.be/oNud52NRsRA)

---
## Prerequisites  
- Python 3.8+  
- pip (Python package installer)  
- Django 4.0+  

---

## Setup Instructions  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/PalthiMalleswari/Url_Shortner.git
   cd urlshortener

2. **Create a Virtual Environment**

    ```bash
   
    python -m venv shortener_env  
    source shortener_env/bin/activate  # On Windows: shortener_env\Scripts\activate

3. **Install Dependencies**

    ```bash
  
    pip install -r requirements.txt

4. **Apply Migrations**

    ```bash
  
    python manage.py makemigrations  
    python manage.py migrate
5. **Run the Development Server**

    ```bash
  
    python manage.py runserver
    Access the Application
Open your browser and navigate to: http://127.0.0.1:8000/

