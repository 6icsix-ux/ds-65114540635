from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)  # รหัสวิชา
    name = models.CharField(max_length=255)  # ชื่อวิชา
    description = models.TextField(blank=True, null=True)  # รายละเอียด
    credits = models.IntegerField()  # จำนวนหน่วยกิต

    def __str__(self):
        return f"{self.code} - {self.name}"
