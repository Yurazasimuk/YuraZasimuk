from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.item.name}"
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def __str__(self):
        return f"Замовлення {self.id} для {self.user.username}"


# store/models.py
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClothingItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# store/models.py
from django.db import models
class Review(models.Model):
    item = models.ForeignKey(ClothingItem, on_delete=models.CASCADE)
    review_text = models.TextField()

    def __str__(self):
        return f'Review for {self.item.name}'
