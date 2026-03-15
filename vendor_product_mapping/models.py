from django.db import models
from core.base_model import BaseModel
from vendor.models import Vendor
from product.models import Product
# Create your models here.
class VendorProductMapping(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE, related_name = 'vendor_products')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'product_vendors')
    primary_mapping = models.BooleanField(default = False)
    class Meta:
        unique_together = ('vendor', 'product')

    def __str__(self):
        return f"{self.vendor.name} -> {self.product.name}"