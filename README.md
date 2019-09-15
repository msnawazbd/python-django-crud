# python-django-crud-application

## Install python first

## Change path from the My computer > Environment Variables
	> Add user variable with python path
	> Add Path (C:\Users\msnaw\AppData\Local\Programs\Python\Python37-32)
## Download (http://bootstrap.pypa.io) get-pip.py
	> run (python get-pip.py)
## Change path from the My computer > Environment Variables
	> Add Path (C:\Users\msnaw\AppData\Local\Programs\Python\Python37-32\Scripts)
  
  > pip install django
  
  > django-admin startproject myproject
  
  > cd myproject
  
  > python manage.py startapp myapp
  
  > python manage.py runserver

## Install MYSQL
	> Download (https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
	> pip install mysqlclient-1.4.4-cp37-cp37m-win32.whl
	> Go to myProject-setting
	> INSTALLED_APPS
	> Set DATABASES

## Make Migration
	> python manage.py makemigrations
	> python manage.py migrate
