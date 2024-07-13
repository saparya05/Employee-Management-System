from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.department


class Position(models.Model):
    position = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.position


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    email_id = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    year_of_experience = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name
    
    
 