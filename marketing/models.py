from django.db import models


class Email(models.Model):
    email = models.EmailField()
