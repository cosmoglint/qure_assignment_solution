from django.db import models

class People(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name()
