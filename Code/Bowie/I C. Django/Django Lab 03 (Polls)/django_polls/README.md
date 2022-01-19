Project requires python >=3.8
1. install requirements
    pip install -r requirements.txt
2. apply migrations
    python manage.py migrate
3. create super user
    python manage.py createsuperuser
4. run server
    python manage.py runserver
5. login into admin with user created in step 3
   check 127.0.0.1:8000/admin
6. add Questions and Choices 
7. check 127.0.0.1:8000/polls