from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)  # 課程名稱
    code = models.CharField(max_length=20, unique=True)  # 課程代號
    teacher_name = models.CharField(max_length=100)  # 教師名稱
    student_name = models.TextField()  # 學生名單
    midscore = models.IntegerField(null=True, blank=True)  # 期中分數
    finalscore = models.IntegerField(null=True, blank=True)  # 期末分數
    credits = models.IntegerField()  # 學分

    def __str__(self):
        return self.name