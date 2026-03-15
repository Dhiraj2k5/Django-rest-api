from rest_framework import serializers
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = ['id', 'course', 'certification', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        instance = self.instance
        course = data.get('course')
        certification = data.get('certification')
        primary = data.get('primary_mapping', False)

        qs = CourseCertificationMapping.objects.filter(course=course, certification=certification)
        if instance:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This course and certification mapping already exists.")

        if primary:
            primary_qs = CourseCertificationMapping.objects.filter(course=course, primary_mapping=True)
            if instance:
                primary_qs = primary_qs.exclude(pk=instance.pk)
            if primary_qs.exists():
                raise serializers.ValidationError("This course already has a primary certification mapping.")

        return data