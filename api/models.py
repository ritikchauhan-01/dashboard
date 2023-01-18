from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    DEPARTMENT_CHOICES = (
        ("External", 'External'),
        ("Internal", 'Internal'),
    )
    employee_type = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    salary = models.IntegerField(default=False, null=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = "profile"
