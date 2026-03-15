from django.db import models
from core.base_model import BaseModel
from product.models import Product
from course.models import Course
# Create your models here.
class ProductCourseMapping(BaseModel):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name= 'product_courses')
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name= 'course_products')
    primary_mapping = models.BooleanField(default = False)
    class Meta:
        unique_together = ('product', 'course')
    def __str__(self):
        return f"{self.product.name} {self.course.name}"