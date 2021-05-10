from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class PromoCode(models.Model):
    CHOICES = (
        ('all', 'All'),
        ('protein', 'Protein'),
        ('vitamins', 'Vitamins'),
        ('supplements', 'Supplements'),
        ('equipment', 'Equipment')
    )

    name = models.CharField(max_length=40)
    code = models.CharField(max_length=20, unique=True)
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),
                                   MaxValueValidator(100)])
    product_type = models.CharField(max_length=11, choices=CHOICES)
    active = models.BooleanField()

    def __str__(self):
        return self.name
