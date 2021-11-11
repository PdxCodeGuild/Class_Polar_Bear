from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField()
    
    def __str__(self):
        return f'{self.text}, {self.is_completed(self.completed)}'

    def is_completed(self, completed):
        if self.completed == 1:
            self.completed = 'Complete'
            
        else:
            self.completed = 'Not complete'
        
        return self.completed