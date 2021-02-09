from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, verbose_name='Категория', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    parent_task = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.category