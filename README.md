Delivery API

A simple RESTful API built with Django REST Framework to manage customers, categories, items, and orders for a delivery service.

Features

CRUD operations on Customers, Categories, Items, and Orders
Uses Django REST Framework's ViewSets and Routers for clean, automatic URL routing
Supports partial updates with PATCH requests
SQLite database for easy setup (can be swapped with other databases)
Example endpoints:
/customers/
/categories/
/items/
/orders/
Getting Started

Prerequisites
Python 3.13+
pip
virtualenv (optional but recommended)
Installation
Clone the repository:
git clone https://github.com/your-username/delivery-api.git
cd delivery-api
Create and activate a virtual environment:
python3 -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Apply migrations to create the database tables:
python manage.py migrate
(Optional) Create a superuser to access the admin panel:
python manage.py createsuperuser
Run the development server:
python manage.py runserver
Usage
Access the API root at: http://127.0.0.1:8000/
Use tools like Postman or curl to interact with the API endpoints.
Supports GET, POST, PUT, PATCH, DELETE requests for resources.
Example: Update Customer's about_them field
curl -X PATCH http://127.0.0.1:8000/customers/1/ -H "Content-Type: application/json" -d '{"about_them": "Loves coffee"}'
Project Structure

delivery_main/ — Django app containing models, views, serializers
delivery_main/models.py — Data models for customers, categories, items, and orders
delivery_main/views.py — ViewSets handling API requests
delivery_main/serializers.py — Serializers to convert models to JSON
delivery_main/urls.py — URL routing using DRF routers
Technologies Used

Python 3.13
Django 5.2.4
Django REST Framework
Next Steps

Add authentication and permissions
Add filtering and pagination
Deploy to a cloud platform like Heroku or AWS
License

This project is licensed under the MIT License.
