from django.db import models


class Application(models.Model):
    """
    Student application need to be approved by dept chair and dean.
    Test workflow
    """
    active = models.BooleanField()
