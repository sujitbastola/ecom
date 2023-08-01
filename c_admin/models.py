# from django.db import models
# from ckeditor.fields import RichTextField

# # Create your models here.
# class Users(models.Model):
#     first_name = models.CharField( max_length=55)
#     last_name = models.CharField( max_length=55)
#     email = models.EmailField( max_length=254)
#     password = models.CharField( max_length=255)
#     created_at = models.DateField(auto_now_add=True)
#     token = models.CharField( max_length=255)
#     is_email_verified = models.BooleanField(default=False)
    
#     def str(self):
#         return self.email
#     # define a method to return the name of the email field
#     # def get_email_field_name(self):
#     #     return 'email'

# class Profile(models.Model):
#     user = models.OneToOneField(Users, on_delete=models.CASCADE)
#     phone_number = models.BigIntegerField(null=True)
#     district = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     street = models.CharField(max_length=50)


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='categorys/')
#     slug = models.SlugField(unique=True)

#     def str(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     slug = models.SlugField(unique=True)
#     description = RichTextField()
#     price = models.DecimalField(max_digits=20, decimal_places=2)
#     quantity = models.IntegerField()
#     brand = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
        
#     def str(self):  
#         return self.name


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='products/')

#     def str(self):
#         return self.product.name + " Image"