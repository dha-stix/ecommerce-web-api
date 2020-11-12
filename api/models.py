from django.db import models

class Category(models.Model):
    CATEGORIES = (
        ("Furnitures","Furnitures"),
        ("Footwears", "Footwears"),
        ("Clothings", "Clothings"),
        ("Accessories", "Accessories"),
        ("Home Appliances", "Home Appliances")
    )
    category = models.CharField(max_length=100, choices=CATEGORIES)

    def __str__(self):
        return f'{self.category} {self.id}'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.FloatField()
    image = models.URLField()

    def __str__(self):
        return self.name
