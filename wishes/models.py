from django.db import models


class BirthdayWishes(models.Model):    
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    birthdate = models.DateField()
    
    def __str__(self):
        return self.username