# blog_site
Site based on Django 1.9, Python 3.
Site is an small blog, where you can write 

## Requirements:
- python module `Django 1.9`
    pip install django==1.9
- SMTP for email delivery (for example you can use `gmail`).

## Preparation:
You shoud create file `secret.py` in `blog_site` folder containing:

    MY_SECRET_KEY = 'xxx' # Secret django key.
    EMAIL_PASSWORD = 'xxx' # Password from your SMTP server.
    EMAIL_USER = 'xxx@xx.xx' # Email from your SMTP server.

## Run:
    python3 manage.py makemigrations blog
    python3 manage.py migrate
    python3 manage.py runserver
