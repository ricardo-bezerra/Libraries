from django.db import models
from uuid import uuid4

class Customer(models.Model):

    id_customer = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=55)
    birth_year = models.DateField()
    location = models.CharField(max_length=25)
    address =  models.CharField(max_length=150)
    job_type = models.CharField(max_length=35)
    create_at = models.DateField(auto_now_add=True)
