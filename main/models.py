from django.db import models


class MainCarousel(models.Model) : 
    id = models.AutoField
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.title

class OfferCarousel(models.Model) : 
    id = models.AutoField
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.title


class Categories(models.Model) : 
    id = models.AutoField
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.name + ' (' + self.category + ')'