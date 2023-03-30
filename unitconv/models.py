from django.db import models


class Operator(models.Model):
    tonsToTroy = models.FloatField()
    gramsToTroy = models.FloatField()
    troyToTroy = models.FloatField()
    kiloToTroy = models.FloatField()
    poundToTroy = models.FloatField()
    ounceToTroy = models.FloatField()

