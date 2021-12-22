from django.db import models


class MainCarousel(models.Model) : 
    main_carousel_id = models.AutoField
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.title

class OfferCarousel(models.Model) : 
    offer_carousel_id = models.AutoField
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="main/images", default="")

    def __str__(self):
        return self.title