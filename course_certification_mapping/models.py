from django.db import models
from core.base_model import BaseModel
from course.models import Course
from certification.models import Certification

class CourseCertificationMapping(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_certifications')
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, related_name='certification_courses')
    primary_mapping = models.BooleanField(default=False)

    class Meta:
        unique_together = ('course', 'certification')

    def __str__(self):
        return f"{self.course.name} → {self.certification.name}"