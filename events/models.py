from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Event(models.Model):
    date_day=models.IntegerField(unique_for_date=None,null=True)
    date_month=models.IntegerField(unique_for_month=None,null=True)
    date_year=models.IntegerField(unique_for_year=None,null=True)
    title=models.CharField(max_length=100)
    desription=models.TextField(max_length=200)


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ["-pk"]
    def __str__(self):
        return self.date_day