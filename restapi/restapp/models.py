from django.db import models

class Drink(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.id + ' ' +self.name + ' ' + self.description
