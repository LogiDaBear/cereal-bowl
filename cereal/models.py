from django.db import models
from django.contrib.auth import get_user_model


class Cereal(models.Model):
    brand = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.brand
