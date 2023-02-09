from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    fk = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    no_hire = models.CharField(max_length=255,)
    is_available = models.BooleanField(max_length=255, blank=True, null=True)
    deactivated_at = models.DateField(auto_now_add=False, blank=True, null=True)
    posted_at = models.DateField(auto_now_add=True, blank=True, null=True)
    post_is_paid = models.BooleanField(max_length=255, default=False, blank=True, null=True)


    def __str__(self):
        return self.title







