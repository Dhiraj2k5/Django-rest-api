from rest_framework import serializers
from .models import VendorProductMapping
class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProductMapping
        fields = ['id', 'vendor' ,'product','primary_mapping' , 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['is_active' , 'created_at' , 'updated_at']
    def validate(self,data):
        instance = self.instance  # None on create, exists on update
        vendor = data.get('vendor')
        product = data.get('product')
        primary = data.get('primary_mapping', False)

        # Duplicate pair check
        qs = VendorProductMapping.objects.filter(vendor=vendor, product=product)
        if instance:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This vendor and product mapping already exists.")

        # Primary mapping check
        if primary:
            primary_qs = VendorProductMapping.objects.filter(vendor=vendor, primary_mapping=True)
            if instance:
                primary_qs = primary_qs.exclude(pk=instance.pk)
            if primary_qs.exists():
                raise serializers.ValidationError("This vendor already has a primary product mapping.")

        return data