from django.db import models
from core.base_model import BaseModel
# Create your models here.

class Course(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique = True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name