# Django-RestFramework-MySql/CrudApplication

Creating a Django Rest Framework (DRF) application with MySQL for CRUD (Create, Read, Update, Delete) operations involves several steps. 
Below are the requirements and steps to create a basic DRF MySQL CRUD application:

#### step01: Python and Django Installation:
* python
* Create a virtual environment (Recommend to use Virtual Environment Wrapper)
* Django (pip install django)
* Django Rest Framework (pip install djangorestframework)
  
#### step02: Database Setup:
* Install Xamp or Wamp Server
* Install MySQL
* Install MySQL client (pip install mysqlclient)
  
#### step03: Django Project Setup:
* django-admin startproject project_name
  
#### step04: Django App Setup:
* cd project_name
* python manage.py startapp app_name
  
#### step05: Database Configuration: 
* Open the settings.py file in your Django project and configure the database setting)
  
#### step06: Model Definition:
* Define your model in the models.py file of your app. This represents the data structure in your database.
  
#### step07: Migration:
* python manage.py makemigrations
* python manage.py migrate
  
#### step08: Configure Serializer, Views, URLs:
* Create a serializer in the serializers.py file to convert your model data to JSON and vice versa.
* Create views in the views.py file to handle CRUD operations using Django Rest Framework classes like APIView and ViewSet.
* Configure URLs in the urls.py file of your app to map views to endpoints.
  
#### step09: Run the Server:
* python manage.py runserver
  
#### step10: Testing project:
* Use tools like Postman to test your CRUD operations on the API endpoints.

## For more details:
1. [Djnago](https://docs.djangoproject.com/en/4.2/)
2. [Django-rest-framework](https://www.django-rest-framework.org/)
3. [React](https://react.dev/learn)
4. [Xamp Server](https://www.apachefriends.org/)
