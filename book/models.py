from django.db import models
from uuid import uuid4

class Book(models.Model):

    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=55)
    release_year = models.DateField()
    state = models.CharField(max_length=15)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=55)
    create_at = models.DateField(auto_now_add=True)
