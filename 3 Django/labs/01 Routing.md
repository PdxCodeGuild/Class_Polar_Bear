# Routing
In this lab we will explore django's routing system. We will be creating a mock portfolio that will link to each of our html/css labs from the first section of the course.

## Version 1
1. Start by creating a django project called labs. This project will be used to contain all of your django labs moving forward.

> django-admin startproject labs

2. Create an app within your labs project named `routing`. We will do this for each lab moving forward.

3. Make sure your new app is listed in the installed apps of your settings.py.

4. Create a path to your new app within your projects urls.py

5. Copy your Bio lab into a templates folder.
> Folder structure should be: app_name/templates/app_name/Bio.html

6. Create a function in views.py to render your Bio html/css lab.

7. Create a path in your apps urls.py to link to your function in your views.

8. Repeat steps 5 through 7 for your Blog, Company and Animations labs.

9. Verify you can visit each page by testing the routes in your browser.

## Version 2
Connect your css style pages to your templates using the static folder.
> ex. app_name/static/app_name/styles.css

Be sure to include `{% load static %}` at the top of each template.

Use the following when linking to your css files:
```html
<link rel="stylesheet" href="{% static 'app_name/styles.css' %}">
```
