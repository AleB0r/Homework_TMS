from django.db import models
from users.models import User


class Laptop(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    video_card = models.ForeignKey('VideoCard', on_delete=models.CASCADE)
    processor = models.ForeignKey('Processor', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    favorites = models.ManyToManyField(User, through='FavoriteLaptop', related_name='favorite_laptops')

    def is_liked_by_user(self, user):
        return self.favorites.filter(id=user.id).exists()

    def __str__(self):
        return f"{self.manufacturer} {self.name} - {self.price}$"


class VideoCard(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    memory = models.IntegerField()
    core_clock = models.FloatField()

    def __str__(self):
        return f"{self.manufacturer} {self.name}"


class Processor(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    cores = models.IntegerField()
    frequency = models.FloatField()

    def __str__(self):
        return f"{self.manufacturer} {self.name}"


class FavoriteLaptop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    laptop = models.ForeignKey('Laptop', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name}'s favorite laptop: {self.laptop.name}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    laptops = models.ManyToManyField(Laptop)

    def __str__(self):
        return f"Cart for {self.user.name}"