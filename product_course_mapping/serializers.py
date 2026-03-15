from rest_framework import serializers
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = ['id', 'product', 'course', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        instance = self.instance
        product = data.get('product')
        course = data.get('course')
        primary = data.get('primary_mapping', False)

        qs = ProductCourseMapping.objects.filter(product=product, course=course)
        if instance:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This product and course mapping already exists.")

        if primary:
            primary_qs = ProductCourseMapping.objects.filter(product=product, primary_mapping=True)
            if instance:
                primary_qs = primary_qs.exclude(pk=instance.pk)
            if primary_qs.exists():
                raise serializers.ValidationError("This product already has a primary course mapping.")

        return data