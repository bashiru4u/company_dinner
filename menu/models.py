from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Upload images to MEDIA_ROOT/food_images/
    image = models.ImageField(
        upload_to='food_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    food = models.ForeignKey(Food, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name='votes', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'food')
