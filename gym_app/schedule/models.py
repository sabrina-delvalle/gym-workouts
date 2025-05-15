from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=400)
    category = models.CharField(max_length=55)
    sets = models.CharField(max_length=25)
    reps = models.CharField(max_length=25)
    image = models.ImageField(default="fallback.png", blank=True)

    def __str__(self):
        return self.name
