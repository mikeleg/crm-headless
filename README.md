# Crm Headless api service in django.

**crm-headless** provides a clean **REST** based API with endpoints for manipulating the customer, note, contact, activity,address.
This project is built on top of **Django** and **Django Rest Framework** and in DDD (Domain Driven Design) approach.

## Features

- API endpoints for **Customer**, **Contact** , **Note** , **Activity** , **Address**

- Documentation for API endpoints using **Swagger**

## How to install

1. **Development enviroment**:
   ```
   pip install -R requirements/dev.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
1. **Production enviroment**:
   ```
   pip install -R requirements/prod.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
