from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser



class Garbage(models.Model):
    pictures = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    number_of_points = models.IntegerField(default=10)
    type_of_garbage = models.CharField(max_length=200)
    where_to_dispose = models.TextField(max_length=200)
    cleaned_by = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    cleaned = models.BooleanField(default=False)

    def __str__(self):
        return self.description




