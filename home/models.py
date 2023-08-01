
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorys/')
    slug = models.SlugField(unique=True)

    def _str_(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def _str_(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    brand = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def _str_(self):
        return self.product.name + " Image"
    
class Users(models.Model):
    first_name = models.CharField( max_length=55)
    last_name = models.CharField( max_length=55)
    # phone=models.BigIntegerField()
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=255)
    created_at = models.DateField(auto_now_add=True)
    token = models.CharField( max_length=255)
    is_email_verified = models.BooleanField(default=False)
    
    def _str_(self):
        return self.email
    # define a method to return the name of the email field
    # def get_email_field_name(self):
    #     return 'email'

class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    date_of_birth = models.DateField()


class CustomDesignedorder(models.Model):
    name = models.CharField( max_length=100)
    image = models.ImageField()

    def _str_(self):
        return self.name + " Image"