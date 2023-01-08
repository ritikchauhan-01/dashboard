from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    DEPARTMENT_CHOICES = (
        ('E' ,' External'),
        ('I', 'Internal'),
    )
    department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES)
    salary = models.IntegerField(default=False, null=False)
    phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = "profile"

