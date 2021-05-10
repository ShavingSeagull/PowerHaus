from django.db import models
from products.models import Product
from profiles.models import Profile


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    content = models.TextField()
    rating = models.CharField(max_length=4, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
