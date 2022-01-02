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
    
    
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
    
    
    
class Cont_info(models.Model):
    id = models.AutoField
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    page = models.CharField(max_length=50)

    def __str__(self):
        return self.phone