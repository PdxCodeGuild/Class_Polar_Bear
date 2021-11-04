from django.db import models

# Create your models here.
class Message(models.Model):
    # django handles ID column by itself
    # each entry represents a column in a table
    text_content = models.CharField(max_length=240)
    user = models.CharField(max_length=40)
    date = models.DateField(auto_created=True) #auto created adds current date when a new message is created

    # we add a str method to print the messages itself instead of "Message object(1)" standard message name
    # With this we can control the way we see our items list in our database
    def __str__(self) -> str:
        return f'{self.date} -- {self.text_content}, {self.user}'


# run python3 manage.py migrate
# to migrate this model use command: python3 manage.py makemigrations
# re run python3 manage.py migrate
# use program DB Browser for SQLite to view your tables/database