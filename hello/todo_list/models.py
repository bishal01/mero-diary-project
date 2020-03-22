from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    item=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

    def _str_(self):
        return self.item + ' | ' + str(self.completed)


