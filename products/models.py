from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=250)
    readable_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_readable_name(self):
        return self.readable_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    sku = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
