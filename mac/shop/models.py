from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20, default="")
    subcategory = models.CharField(max_length=20, default="")
    price = models.IntegerField(default=0)
    decs = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=20, default="")
    message = models.CharField(max_length=200, default="")

