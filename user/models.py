from django.db import models
from uuid import uuid4

class User(models.Model):

    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    serial_number = models.CharField(max_length=35)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=55)
    birth_year = models.DateField()
    location = models.CharField(max_length=25)
    address =  models.CharField(max_length=150)
    business_unity = models.CharField(max_length=35)
    create_at = models.DateField(auto_now_add=True)
