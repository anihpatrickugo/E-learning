# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class Course(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     course_code = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return f"{self.name} {self.course_code}"


# class Lecturer(User, models.Model):
#     course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
    
# class Student(User, models.Model):
#     course_offered = models.ForeignKey(Course, related_name='registered_course', on_delete=models.CASCADE)
#     registered = False

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def register(self):
#         if self.course_offered:
#             self.registered = True
#             super().save()








    

