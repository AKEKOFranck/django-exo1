from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Students(models.Model):
    name = models.fields.CharField(max_length=100, null=False)
    first_name = models.fields.CharField(max_length=500, null=False)
    age = models.fields.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(20)], null=False)
    math = models.fields.FloatField(validators=[MinValueValidator(5), MaxValueValidator(20)], null=False)
    french = models.fields.FloatField(validators=[MinValueValidator(5), MaxValueValidator(20)], null=False)
    anglais = models.fields.FloatField(validators=[MinValueValidator(5), MaxValueValidator(20)], null=False)

    def moyenne(self):
        return (self.math + self.french + self.anglais) / 3 