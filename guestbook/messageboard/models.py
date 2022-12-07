from django.db import models

class Messageboard(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    postdate = models.DateField(auto_now=True)
    