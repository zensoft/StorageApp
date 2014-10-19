from django.db import models

class GroupModel(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=30)
    descriptions_test = models.CharField(max_length=30)
